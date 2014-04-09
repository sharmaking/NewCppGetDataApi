import GetApiPythonLib

def main():
	p_api = GetApiPythonLib.PyGetDataApi()
	p_spi = GetApiPythonLib.PyGetDataSpi()
	print dir(GetApiPythonLib)

	if p_api.PyInitConnection("180.166.168.126",18201,p_spi):
		_list = ["600000","600001","000004"]
		p_api.PySubStockCode(False,_list)
		
		p_api.PyReqTodayData(1, 0)

	while 1:
		pass



if __name__ == '__main__':
	main()