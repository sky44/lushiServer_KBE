# -*- coding: utf-8 -*-
import KBEngine
import d_card_dis
import random
import re
from KBEDebug import *
from array import *


class BattleField(KBEngine.Entity):
    def __init__(self):
        KBEngine.Entity.__init__(self)
        DEBUG_MSG("BattleField.cell[%i].init" %(self.id))
        self.player0=None
        self.player1=None

    def AvatarRegiste(self,avatarEntity,playerID):
        DEBUG_MSG("BattleField.cell[%i].AvatarRegiste entityID:[%s]" %(self.id,avatarEntity.id))
        if(playerID==1):
            self.player1=avatarEntity
        else:
            self.player0=avatarEntity
        if(self.player0!=None and self.player1!=None):
            self.players={
                self.player0,
                self.player1
            }
        self.startBattle()
    def startBattle(self):
        DEBUG_MSG("BattleField.cell[%i].startBattle" %(self.id))
        self.round=0
        self.currentPlayer=0
        self.giveCard(0,20000002)
        slef.players[0].getCardFromKz(3)
        slef.players[1].getCardFromKz(3)
        self.nextRound()
    def nextRound(self):
        DEBUG_MSG("BattleField.cell[%i].nextRound" %(self.id))
        self.round+=1
        self.currentPlayer=(self.round+1)%2
        slef.players[self.currentPlayer].setSituation(1)
        self.players[self.another(self.currentPlayer)].setSituation(0)
    def endRound(self):
        DEBUG_MSG("BattleField.cell[%i].endRound" %(self.id))
        self.nextRound()
    def giveCard(self,playerID,cardID):
        DEBUG_MSG("BattleField.cell[%i].giveCard playerID[%s] cardID:[%s]" %(self.id,playerID,cardID))
        self.players[playerID].getCard(20000002)
    def another(self,id):
        if id==0:
            return 1
        else:
            return 0
    def getAllEntity(self):
        return self.player0.cardEntityList+self.player1.cardEntityList