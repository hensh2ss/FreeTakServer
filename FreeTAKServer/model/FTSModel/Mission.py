#######################################################
# 
# Mission.py
# Python implementation of the Class Mission
# Generated by Enterprise Architect
# Created on:      11-Feb-2020 11:08:08 AM
# Original author: Corvo
# 
#######################################################
from FreeTAKServer.model.FTSModelVariables.MissionVariables import MissionVariables as vars
from FreeTAKServer.model.FTSModel.MissionChanges import MissionChanges

class Mission:
    def __init__(self):
        self.type = None

        self.tool = None

        self.name = None

        self.authorUid = None

    @staticmethod
    def CreateExCheckTemplate(TYPE=vars.CreateExCheckTemplate().TYPE, TOOL=vars.CreateExCheckTemplate().TOOL,
                              NAME=vars.CreateExCheckTemplate().NAME,
                              AUTHORUID=vars.CreateExCheckTemplate().AUTHORUID, ):
        mission = Mission()

        mission.settype(TYPE)

        mission.settool(TOOL)

        mission.setname(NAME)

        mission.setauthorUid(AUTHORUID)

        mission.missionchanges = MissionChanges.CreateExCheckTemplate()

        return mission

    def settype(self, type):
        self.type = type

    def gettype(self):
        return self.type

    def settool(self, tool):
        self.tool = tool

    def gettool(self):
        return self.tool

    def setname(self, name):
        self.name = name

    def getname(self):
        return self.name

    def setauthorUid(self, authorUid):
        self.authorUid = authorUid

    def getauthorUid(self):
        return self.authorUid

if __name__ == "__main__":
    y = Mission.CreateExCheckTemplate()