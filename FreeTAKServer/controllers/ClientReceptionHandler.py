#######################################################
# 
# ClientReceptionHandler.py
# Python implementation of the Class ClientReceptionHandler
# Generated by Enterprise Architect
# Created on:      19-May-2020 7:17:21 PM
# Original author: Natha Paquette
# 
#######################################################
import time
import socket
import errno
import copy
import re
import sys

from FreeTAKServer.controllers.CreateLoggerController import CreateLoggerController
from FreeTAKServer.controllers.configuration.LoggingConstants import LoggingConstants
from defusedxml import ElementTree as etree

loggingConstants = LoggingConstants(log_name="FTS_ClientReceptionHandler")
logger = CreateLoggerController("FTS_ClientReceptionHandler", logging_constants=loggingConstants).getLogger()
from FreeTAKServer.controllers.configuration.ClientReceptionLoggingConstants import ClientReceptionLoggingConstants

loggingConstants = ClientReceptionLoggingConstants()


class ClientReceptionHandler:
    def __init__(self):
        self.dataPipe = []
        self.socketCount = 0

    def startup(self, clientInformationArray):
        try:
            self.clientInformationArray = clientInformationArray  # create copy of client information array so it cant be changed during iteration
            '''logger.propagate = False
            logger.info(loggingConstants.CLIENTRECEPTIONHANDLERSTART)
            logger.propagate = True'''
            output = self.monitorForData(self.dataPipe)
            if output == 1:
                return self.dataPipe
            else:
                return -1
            '''
            time.sleep(600)
            # temporarily remove due to being unnecessary and excessively flooding logs
            logger.info('the number of threads is ' + str(threading.active_count()) + ' monitor event process alive is ' + str(monitorEventProcess.is_alive()) +
                        ' return data to Orchestrator process alive is ' + str(monitorForData.is_alive()))
            '''
        except Exception as e:
            logger.error(loggingConstants.CLIENTRECEPTIONHANDLERSTARTUPERROR + str(e))

    def monitorForData(self, queue):
        '''
        updated receive all
        '''
        try:
            keys = copy.deepcopy(list(self.clientInformationArray.keys()))  # this prevents changes to the clientInformationArray from having any severe effects on this method
            for user_id in keys:
                sock = self.clientInformationArray[user_id][0]
                client = self.clientInformationArray[user_id][1]
                try:
                    try:
                        BUFF_SIZE = 8087
                        data = b''
                    except Exception as e:
                        print('\n\n disconnect A \n\n')
                        logger.error(loggingConstants.CLIENTRECEPTIONHANDLERMONITORFORDATAERRORA + str(e))
                        self.returnReceivedData(client, b'', queue)
                    try:
                        sock.setblocking(0)  # prevents blocking if there is no data to be read
                        part = sock.recv(1)
                        sys.stdout.flush()
                    except socket.timeout as e:
                        continue
                    except BrokenPipeError as e:
                        print('\n\n disconnect B \n\n')
                        self.returnReceivedData(client, b'', queue)
                        continue
                    except socket.error as e:
                        if hasattr(e, "errno") and e.errno == errno.EWOULDBLOCK:  # this prevents errno 11 from spontanieously disconnecting clients due to the socket blocking set to 0
                            # logger.debug("EWOULDBLOCK error passed " + str(e))
                            continue
                        elif hasattr(e, "errno") and e.errno == errno.ECONNRESET:
                            print('econ reset passed')
                            continue
                        else:
                            self.returnReceivedData(client, b'', queue)
                            continue
                    except Exception as e:
                        import traceback

                        print('\n\n disconnect C ' + str(e) + "\n\n")
                        logger.error(
                            "Exception other than broken pipe in monitor for data function " + str(e) + ''.join(traceback.format_exception(None, e, e.__traceback__)))
                        self.returnReceivedData(client, b'', queue)
                        continue
                    try:
                        if part == b'' or part is None:
                            print('\n\n disconnect D \n\n')
                            logger.debug("empty string sent, standard disconnect")
                            self.returnReceivedData(client, b'', queue)
                            continue
                        else:
                            try:
                                client_file = sock.makefile()  # get file descriptor so socket can be read without delay
                                xmlstring = part.decode() + client_file.read()
                                xmlstring = "<multiEvent>" + xmlstring + "</multiEvent>"  # convert to xmlstring wrapped by multiEvent tags
                                xmlstring = re.sub(r'\<\?xml(?s)(.*)\?\>', '', xmlstring)  # replace xml definition tag with empty string as it breaks serilization
                                events = etree.fromstring(xmlstring)  # serialize to object
                                for event in events.findall('event'):
                                    self.returnReceivedData(client, etree.tostring(event), queue)  # send each instance of event to the core
                            except Exception as e:
                                logger.error('error in buffer ' + str(e))
                                # return -1 commented out so entire run isn't stopped because of one disconnect

                    except Exception as e:
                        print('\n\n disconnect F \n\n')
                        logger.error(loggingConstants.CLIENTRECEPTIONHANDLERMONITORFORDATAERRORC + str(e))
                        self.returnReceivedData(client, b'', queue)
                        # self.clientInformationArray.remove(client) commented out so size doesnt change during iteration
                        # return -1 commented out so entire run isn't stopped because of one disconnect

                except Exception as e:
                    print(f'\n\n disconnect G {str(e)} \n\n')
                    logger.error(loggingConstants.CLIENTRECEPTIONHANDLERMONITORFORDATAERRORD + str(e))
                    self.returnReceivedData(client, b'', queue)
                    # return -1 commented out so entire run isn't stopped because of one disconnect
            return 1
        except Exception as e:
            logger.error('exception in monitor for data ' + str(e))
            return -1

    def returnReceivedData(self, clientInformation, data, queue):
        try:
            from FreeTAKServer.model.RawCoT import RawCoT
            # print(data)
            RawCoT = RawCoT()
            RawCoT.clientInformation = clientInformation
            RawCoT.xmlString = data.replace(b'\n', b'')  # replace all newlines with empty
            self.dataPipe.append(RawCoT)
            # logger.debug("data: "+ str(data)+" received from: "+clientInformation.user_id)
            return 1
        except Exception as e:
            logger.error(loggingConstants.CLIENTRECEPTIONHANDLERRETURNRECEIVEDDATAERROR + str(e))
            return -1
