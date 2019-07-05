#coding:utf-8

import os
import shutil
import sys
import time
import json
import logging

logger = logging.getLogger("Sub")

class ExporterWps(object):
	def __init__(self, result):
		self.__results = result

	def export(self):
		nowTime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
		fileloc = "./results/" + nowTime
		res = "var res = " + json.dumps(self.__results,sort_keys=True,indent=4,separators=(',',':'))
		if (os.path.exists(fileloc)):
			shutil.rmtree(fileloc)
		shutil.copytree("./resources/template/", fileloc)
		filename = os.path.join(fileloc, "results.js")
		with open(filename,"w+",encoding="utf-8") as f:
			f.writelines(res)
			f.close()
		indexFilename = os.path.join(fileloc, "index.html")
		index = ""
		read = []
		with open(indexFilename, "r", encoding="utf-8") as f:
			read = f.readlines()
			f.close()
		for r in read:
			index += r
		index = index.replace(r"{{ $generatedTime }}", nowTime)
		with open(indexFilename, "w+", encoding="utf-8") as f:
			f.writelines(index)
			f.close()
		logger.info("Web page simulation result exported as %s" % fileloc)

