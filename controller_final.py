#!/usr/bin/env python
# ************************************************************************
#
# (C) COPYRIGHT 2014-2015 TECHNOLUTION BV, GOUDA NL
#   =======          I                   ==          I    =
#      I             I                    I          I
# |    I   ===   === I ===  I ===   ===   I  I    I ====  I   ===  I ===
# |    I  /   \ I    I/   I I/   I I   I  I  I    I  I    I  I   I I/   I
# |    I  ===== I    I    I I    I I   I  I  I    I  I    I  I   I I    I
# |    I  \     I    I    I I    I I   I  I  I   /I  \    I  I   I I    I
# |    I   ===   === I    I I    I  ===  ===  === I   ==  I   ===  I    I
# |                 +---------------------------------------------------+
# +----+            |  +++++++++++++++++++++++++++++++++++++++++++++++++|
#      |            |             ++++++++++++++++++++++++++++++++++++++|
#      +------------+                          +++++++++++++++++++++++++|
#                                                         ++++++++++++++|
#                                                                  +++++|
#
# ************************************************************************


import time
import threading
import matplotlib.pyplot as plt
import socket

wp_reached_detail = {}
logging_list = {}
global_preference = {}

from behaviours_final import Behaviour
from robot_model_change_in_progress import Model
from V2V_final import V2V_comm
from interface_change_in_progress import Interface
from dms_communication import DmsInterface
from Fake_MC import waypoints, initial_pos
from collections import deque

current_milli_time = lambda: int(round(time.time()*1000))

""" A controller for a mobile robot.
    The controller loops and determines which behavior should be performed.

    Original author: Martijn van den Heuvel(martijn.van.den.heuvel@technolution.nl)
    Edited by: Lenin Mishra(leninmishra92@gmail.com)
"""
# *************************************************************************** #
# Classes.
# *************************************************************************** #


class carThread(threading.Thread):
    global wp_reached_detail
    global logging_list
    # ********************************************************************* #
    #
    def __init__(self,number_of_vehicles, threadID, name, port, v2v_port):
        threading.Thread.__init__(self)
        self.number_of_vehicles=number_of_vehicles
        self.threadID = threadID
        self.name = name
        self.port = port
        self.v2v_port = v2v_port
        self.wp_list=[]
        self.wp_time_list = []
        self.comm = V2V_comm(self.v2v_port, self.number_of_vehicles)
        self.destination_reached = False
        self.destination = 0
        self.collided = False
        self.optimizing = False
        self.speed_track = []
        self.start_time = 0
        self.present_time = 0
        self._running = False
        self.intersection_found = False

        self.comm.creating_ports()
        #self.comm.creating_empty_lists_for_Tc()

    def run(self):

        #print "Starting " + self.name
        #print"The number of vehicles in the arena are: ", self.number_of_vehicles
        self._running = True
        self.wp_list=waypoints(self.threadID)
        self.destination = self.wp_list[-1]
        self.tme_to_wp()
        self.comm.creating_empty_lists(self.wp_time_list)

        # initialize interface
        interface = Interface(port=self.port)

        #v2v = V2V_comm(port = self.v2v_port)
        sensor_ok = False
        while not sensor_ok:
            try:
                interface.subscribe_to_sensor_data()
                interface.get_latest_sensor_data()
                sensor_ok = True
                #print "sensor okay"
                #print 'Got sensor data for %s' % self.name
                #self.send_data.sendto(interface.get_latest_sensor_data(),(host,5000+self.threadID))
            except Exception as e:
                print("%s fail subscribe sensors: %s" % (self.name, e))
            #time.sleep(1)
        #print 'Got sensor data for %s' % self.name
        # Communication with DriveModeSelector
        dms = DmsInterface(self.threadID)
        dms.start()
        # initialize model of the robot
        model = Model(interface, dms, initial_pos(self.threadID))
        #time.sleep(1)
        # initialize behaviours
        behaviour = Behaviour(model,self.comm)
        if self.number_of_vehicles > 1:
            self.comm.sending_data(self.wp_time_list,'wp')
            r1 = self.comm.receiving_data()
            decision, intersection_detail = self.comm.identify_ib_with_line()
            tme = self.comm.calculate_time_to_collision(30,[self.wp_time_list[0][0][0],self.wp_time_list[0][0][1]],intersection_detail)
            self.comm.creating_lists_for_Tc(tme)
            self.comm.sending_data(tme,'tc')
            r2 = self.comm.receiving_data()
        elif self.number_of_vehicles == 1:
            decision = False
        self.start_time = current_milli_time()
        #result = behaviour.collision_check()
        while not dms.is_done():
            if len(self.wp_list) != 1:
                waypoint1 = self.wp_list.pop(1)

                if decision == True:
                    #print "Decision is true"
                    command = self.comm.intersection_strategy()
                    #speed = self.determine_speed(new_time)
                    goal,collision_check = self.drive_waypoints(interface, behaviour, waypoint1, command)
                    if collision_check == True:
                        self.collided = True
                        print "Collision happened"
                        break
                    else:
                        continue
##                    if goal == True and collision_check == False:
##                        continue
##                    if collision_check== True:
##                        self.collided = True
##                        print "Collision happened"
##                        break
                elif decision == False:
                    goal = self.drive_waypoints(interface, behaviour, waypoint1, None)
                    if goal == True:
                        continue
            elif len(self.wp_list) == 1:
                print "No more waypoints for vehicle:",self.threadID
                self.destination_reached = True

                model.update_sensors()
                interface.send_drive_message(0, 0)
                break
        #print('No more waypoints. End of the line.')
        #self.comm.number_of_vehicles -= 1
        #if self.collided == False:
            #print "No collision for vehicle:",self.port
        if self.collided == True:
            print "Collision happened for vehicle:",self.port
        end_of_simulation(self.port-10150)
        logging(self.port-10150,model.log)
        while all(val==True for val in wp_reached_detail.values()) != True:
            behaviour.collision_check(True,self.destination)
##        if all(val==True for val in wp_reached_detail.values()) == True:
##            self.comm.skt.shutdown(socket.SHUT_RDWR)
##            self.comm.skt.close()
        #behaviour.destination_reached = True
        #print g_car_yaw.actual_data
        print model.log
        dms.stop()
        return

        #if all(val==True for val in wp_reached_detail.values()) == True:
##        if all(val==True for val in wp_reached_detail.values()) == True:
##            self.close()

    # ********************************************************************* #
    #
    def drive_waypoints(self, interface, behaviour, waypoint, command):
        """ makes the vehicle go to several goals """
        #self.start_time = time.time()
        goal_reached = False
        collision_check = False
        goal_x, goal_y, speed = waypoint
        if command == None:
            command = speed

        print "My vehicle id and speed are: ", (self.threadID, command)
        if self.number_of_vehicles == 1:
            while not goal_reached:
                steering_angle, goal_reached = behaviour.go_to_goal(goal_x, goal_y)
                interface.send_drive_message(command, steering_angle)
                collision_check = False
        elif self.number_of_vehicles > 1:
            while not goal_reached and not collision_check:
                steering_angle, goal_reached = behaviour.go_to_goal(goal_x, goal_y)
                collision_check = behaviour.collision_check(self.destination_reached,self.destination)
                self.optimizing = self.comm.optimization_check()
                self.intersection_found = self.comm.intersection_check()
                if self.intersection_found == False:
                    interface.send_drive_message(speed, steering_angle)
                elif self.intersection_found == True:
                    if self.optimizing == False:
                        #print "Not yet optimized"
                        interface.send_drive_message(command, steering_angle)
                        self.speed_track.append((command,current_milli_time()))
                    elif self.optimizing == True:
                        #print "Already optimized"
                        interface.send_drive_message(speed, steering_angle)
                        self.speed_track.append((speed,current_milli_time()))
                elif collision_check == True:
                    break
##            elif goal_reached == True: #and len(self.wp_list)!=1:
##                return goal_reached,collision_check
        return goal_reached, collision_check

    def tme_to_wp(self):
        reach_goal_time = 0
        self.wp_time_list.append([self.wp_list[0],reach_goal_time])
        for index in range(0,len(self.wp_list)-1):
            distance = ((self.wp_list[index][0]-self.wp_list[index+1][0])**2+(self.wp_list[index][1]-self.wp_list[index+1][1])**2)**0.5
            time = distance/self.wp_list[index][2]
            reach_goal_time+=time
            x=[self.wp_list[index+1],reach_goal_time]
            self.wp_time_list.append(x)



def end_of_simulation(vehicle_number):
    global wp_reached_detail
    wp_reached_detail["Vehicle"+str(vehicle_number)] = True

def logging(vehicle_number,data):
    global logging_list
    logging_list["Vehicle"+str(vehicle_number)] = data



if __name__ == '__main__':
    GCONTROL_BASE_UDP_PORT = 10150
    NR_CARS = 3
    for number in range(1,NR_CARS+1):
        wp_reached_detail["Vehicle"+str(number)] = False
        logging_list["Vehicle"+str(number)] = []
        global_preference["Vehicle"+str(number)] = []
    #adding code for V2V communication
    V2VCONTROL_SERVER = 30150
    #next_wp = (0,-10,1)
    cars = []
    for carId in range(1, NR_CARS +1):
        cars.append(carThread(NR_CARS, carId, "thread-%d" % carId, GCONTROL_BASE_UDP_PORT + carId, V2VCONTROL_SERVER+carId))
    for car in cars:
        #car.setDaemon(True)
        car.start()




