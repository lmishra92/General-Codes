import win32com.client as com
def startVissim():
	try:
		return com.dynamic.Dispatch('Vissim.Vissim.700')
	except:
		return 'StartError'
		
		
