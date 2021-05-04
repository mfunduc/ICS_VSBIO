def ConvertNetworkStringToID (NetworkString):
	networkNames = [ 
		["neoVI", 0],
		["HSCAN", 1],
		["MSCAN", 2],
		["SWCAN", 3],
		["LSFTCAN", 4],
		["FORDSCP", 5],
		["J1708", 6],
		["AUX", 7],
		["JVPW", 8],
		["ISO", 9],
		["ISOPIC", 10],
		["MAIN51", 11],
		["RED", 12],
		["SCI", 13],
		["ISO2", 14],
		["ISO14230", 15],
		["LIN", 16],
		["OP_ETHERNET1", 17],
		["OP_ETHERNET2", 18],
		["OP_ETHERNET3", 19],
		["ISO3", 41],
		["HSCAN2", 42],
		["HSCAN3", 44],
		["OP_ETHERNET4", 45],
		["OP_ETHERNET5", 46],
		["ISO4", 47],
		["LIN2", 48],
		["LIN3", 49],
		["LIN4", 50],
		["MOST", 51],
		["RED_APP_ERROR", 52],
		["CGI", 53],
		["3G_RESET_STATUS", 54],
		["3G_FB_STATUS", 55],
		["3G_APP_SIGNAL_STATU", 56],
		["3G_READ_DATALINK_CM_TX_MSG", 57],
		["3G_READ_DATALINK_CM_RX_MSG", 58],
		["3G_LOGGING_OVERFLOW", 59],
		["3G_READ_SETTINGS_EX", 60],
		["HSCAN4", 61],
		["HSCAN5", 62],
		["RS232", 63],
		["UART", 64],
		["UART2", 65],
		["UART3", 66],
		["UART4", 67],
		["SWCAN2", 68],
		["ETHERNET_DAQ", 69],
		["DATA_TO_HOST", 70],
		["I2C1", 71],
		["SPI1", 72],
		["OP_ETHERNET6", 73],
		["RED_VBAT", 74],
		["OP_ETHERNET7", 75],
		["OP_ETHERNET8", 76],
		["OP_ETHERNET9", 77],
		["OP_ETHERNET10", 78],
		["OP_ETHERNET11", 79],
		["FLEXRAY1A", 80],
		["FLEXRAY1B", 81],
		["FLEXRAY2A", 82],
		["FLEXRAY2B", 83],
		["LIN5", 84],
		["FLEXRAY", 85],
		["FLEXRAY2", 86],
		["OP_ETHERNET12", 87],
		["MOST25", 90],
		["MOST50", 91],
		["MOST150", 92],
		["ETHERNET", 93],
		["GMFSA", 94],
		["TCP", 95],
		["HSCAN6", 96],
		["HSCAN7", 97],
		["LIN6", 98],
		["LSFTCAN2", 99] ]
	for x, sublist in enumerate(networkNames):
		if NetworkString == sublist[0]:
			return sublist[1]
	return (-1)