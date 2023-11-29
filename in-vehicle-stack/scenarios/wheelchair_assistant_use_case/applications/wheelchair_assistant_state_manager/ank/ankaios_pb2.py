# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ank/ankaios.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61pi/ankaios.proto\x12\x07\x61nkaios\"\xae\x02\n\x12StateChangeRequest\x12)\n\nagentHello\x18\x01 \x01(\x0b\x32\x13.ankaios.AgentHelloH\x00\x12;\n\x13updateWorkloadState\x18\x02 \x01(\x0b\x32\x1c.ankaios.UpdateWorkloadStateH\x00\x12\x32\n\x0bupdateState\x18\x03 \x01(\x0b\x32\x1b.ankaios.UpdateStateRequestH\x00\x12=\n\x14requestCompleteState\x18\x04 \x01(\x0b\x32\x1d.ankaios.RequestCompleteStateH\x00\x12#\n\x07goodbye\x18\x05 \x01(\x0b\x32\x10.ankaios.GoodbyeH\x00\x42\x18\n\x16stateChangeRequestEnum\"\xcb\x01\n\x10\x45xecutionRequest\x12\x31\n\x0eupdateWorkload\x18\x01 \x01(\x0b\x32\x17.ankaios.UpdateWorkloadH\x00\x12;\n\x13updateWorkloadState\x18\x02 \x01(\x0b\x32\x1c.ankaios.UpdateWorkloadStateH\x00\x12/\n\rcompleteState\x18\x03 \x01(\x0b\x32\x16.ankaios.CompleteStateH\x00\x42\x16\n\x14\x65xecutionRequestEnum\"\x1f\n\nAgentHello\x12\x11\n\tagentName\x18\x01 \x01(\t\"\t\n\x07Goodbye\"t\n\x0eUpdateWorkload\x12.\n\x0e\x61\x64\x64\x65\x64Workloads\x18\x01 \x03(\x0b\x32\x16.ankaios.AddedWorkload\x12\x32\n\x10\x64\x65letedWorkloads\x18\x02 \x03(\x0b\x32\x18.ankaios.DeletedWorkload\"\xdd\x02\n\rAddedWorkload\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07runtime\x18\x02 \x01(\t\x12>\n\x0c\x64\x65pendencies\x18\x03 \x03(\x0b\x32(.ankaios.AddedWorkload.DependenciesEntry\x12\x0f\n\x07restart\x18\x04 \x01(\x08\x12/\n\x0eupdateStrategy\x18\x05 \x01(\x0e\x32\x17.ankaios.UpdateStrategy\x12+\n\x0c\x61\x63\x63\x65ssRights\x18\x06 \x01(\x0b\x32\x15.ankaios.AccessRights\x12\x1a\n\x04tags\x18\x07 \x03(\x0b\x32\x0c.ankaios.Tag\x12\x15\n\rruntimeConfig\x18\x08 \x01(\t\x1aK\n\x11\x44\x65pendenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0e\x32\x16.ankaios.ExpectedState:\x02\x38\x01\"\xae\x01\n\x0f\x44\x65letedWorkload\x12\x0c\n\x04name\x18\x01 \x01(\t\x12@\n\x0c\x64\x65pendencies\x18\x02 \x03(\x0b\x32*.ankaios.DeletedWorkload.DependenciesEntry\x1aK\n\x11\x44\x65pendenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0e\x32\x16.ankaios.ExpectedState:\x02\x38\x01\"i\n\rWorkloadState\x12\x14\n\x0cworkloadName\x18\x01 \x01(\t\x12\x11\n\tagentName\x18\x02 \x01(\t\x12/\n\x0e\x65xecutionState\x18\x03 \x01(\x0e\x32\x17.ankaios.ExecutionState\"E\n\x13UpdateWorkloadState\x12.\n\x0eworkloadStates\x18\x01 \x03(\x0b\x32\x16.ankaios.WorkloadState\"\x9e\x01\n\rCompleteState\x12\x11\n\trequestId\x18\x01 \x01(\t\x12$\n\x0cstartupState\x18\x02 \x01(\x0b\x32\x0e.ankaios.State\x12$\n\x0c\x63urrentState\x18\x03 \x01(\x0b\x32\x0e.ankaios.State\x12.\n\x0eworkloadStates\x18\x04 \x03(\x0b\x32\x16.ankaios.WorkloadState\"<\n\x14RequestCompleteState\x12\x11\n\trequestId\x18\x01 \x01(\t\x12\x11\n\tfieldMask\x18\x02 \x03(\t\"R\n\x12UpdateStateRequest\x12(\n\x08newState\x18\x01 \x01(\x0b\x32\x16.ankaios.CompleteState\x12\x12\n\nupdateMask\x18\x02 \x03(\t\"\xcf\x02\n\x05State\x12\x30\n\tworkloads\x18\x01 \x03(\x0b\x32\x1d.ankaios.State.WorkloadsEntry\x12,\n\x07\x63onfigs\x18\x02 \x03(\x0b\x32\x1b.ankaios.State.ConfigsEntry\x12.\n\x08\x63ronjobs\x18\x03 \x03(\x0b\x32\x1c.ankaios.State.CronjobsEntry\x1a\x43\n\x0eWorkloadsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.ankaios.Workload:\x02\x38\x01\x1a.\n\x0c\x43onfigsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x41\n\rCronjobsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.ankaios.Cronjob:\x02\x38\x01\"\xd4\x02\n\x08Workload\x12\r\n\x05\x61gent\x18\x01 \x01(\t\x12\x0f\n\x07restart\x18\x02 \x01(\x08\x12\x39\n\x0c\x64\x65pendencies\x18\x03 \x03(\x0b\x32#.ankaios.Workload.DependenciesEntry\x12/\n\x0eupdateStrategy\x18\x04 \x01(\x0e\x32\x17.ankaios.UpdateStrategy\x12\x1a\n\x04tags\x18\x05 \x03(\x0b\x32\x0c.ankaios.Tag\x12+\n\x0c\x61\x63\x63\x65ssRights\x18\x06 \x01(\x0b\x32\x15.ankaios.AccessRights\x12\x0f\n\x07runtime\x18\x07 \x01(\t\x12\x15\n\rruntimeConfig\x18\x08 \x01(\t\x1aK\n\x11\x44\x65pendenciesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0e\x32\x16.ankaios.ExpectedState:\x02\x38\x01\"!\n\x03Tag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"a\n\x0c\x41\x63\x63\x65ssRights\x12(\n\x05\x61llow\x18\x01 \x03(\x0b\x32\x19.ankaios.AccessRightsRule\x12\'\n\x04\x64\x65ny\x18\x02 \x03(\x0b\x32\x19.ankaios.AccessRightsRule\"a\n\x10\x41\x63\x63\x65ssRightsRule\x12*\n\toperation\x18\x01 \x01(\x0e\x32\x17.ankaios.PatchOperation\x12\x12\n\nupdateMask\x18\x02 \x03(\t\x12\r\n\x05value\x18\x03 \x03(\t\"@\n\x07\x43ronjob\x12\x10\n\x08workload\x18\x01 \x01(\t\x12#\n\x08interval\x18\x02 \x01(\x0b\x32\x11.ankaios.Interval\";\n\x08Interval\x12\r\n\x05hours\x18\x01 \x01(\r\x12\x0f\n\x07minutes\x18\x02 \x01(\r\x12\x0f\n\x07seconds\x18\x03 \x01(\r*)\n\rExpectedState\x12\x0b\n\x07STOPPED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01*}\n\x0e\x45xecutionState\x12\x10\n\x0c\x45XEC_PENDING\x10\x00\x12\x10\n\x0c\x45XEC_RUNNING\x10\x01\x12\x12\n\x0e\x45XEC_SUCCEEDED\x10\x02\x12\x0f\n\x0b\x45XEC_FAILED\x10\x03\x12\x10\n\x0c\x45XEC_UNKNOWN\x10\x04\x12\x10\n\x0c\x45XEC_REMOVED\x10\x05*F\n\x0eUpdateStrategy\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x11\n\rAT_LEAST_ONCE\x10\x01\x12\x10\n\x0c\x41T_MOST_ONCE\x10\x02*2\n\x0ePatchOperation\x12\x0b\n\x07REPLACE\x10\x00\x12\x07\n\x03\x41\x44\x44\x10\x01\x12\n\n\x06REMOVE\x10\x02\x32]\n\x0f\x41gentConnection\x12J\n\x0c\x43onnectAgent\x12\x1b.ankaios.StateChangeRequest\x1a\x19.ankaios.ExecutionRequest(\x01\x30\x01\x32Y\n\rCliConnection\x12H\n\nConnectCli\x12\x1b.ankaios.StateChangeRequest\x1a\x19.ankaios.ExecutionRequest(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ank.ankaios_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ADDEDWORKLOAD_DEPENDENCIESENTRY']._options = None
  _globals['_ADDEDWORKLOAD_DEPENDENCIESENTRY']._serialized_options = b'8\001'
  _globals['_DELETEDWORKLOAD_DEPENDENCIESENTRY']._options = None
  _globals['_DELETEDWORKLOAD_DEPENDENCIESENTRY']._serialized_options = b'8\001'
  _globals['_STATE_WORKLOADSENTRY']._options = None
  _globals['_STATE_WORKLOADSENTRY']._serialized_options = b'8\001'
  _globals['_STATE_CONFIGSENTRY']._options = None
  _globals['_STATE_CONFIGSENTRY']._serialized_options = b'8\001'
  _globals['_STATE_CRONJOBSENTRY']._options = None
  _globals['_STATE_CRONJOBSENTRY']._serialized_options = b'8\001'
  _globals['_WORKLOAD_DEPENDENCIESENTRY']._options = None
  _globals['_WORKLOAD_DEPENDENCIESENTRY']._serialized_options = b'8\001'
  _globals['_EXPECTEDSTATE']._serialized_start=2758
  _globals['_EXPECTEDSTATE']._serialized_end=2799
  _globals['_EXECUTIONSTATE']._serialized_start=2801
  _globals['_EXECUTIONSTATE']._serialized_end=2926
  _globals['_UPDATESTRATEGY']._serialized_start=2928
  _globals['_UPDATESTRATEGY']._serialized_end=2998
  _globals['_PATCHOPERATION']._serialized_start=3000
  _globals['_PATCHOPERATION']._serialized_end=3050
  _globals['_STATECHANGEREQUEST']._serialized_start=31
  _globals['_STATECHANGEREQUEST']._serialized_end=333
  _globals['_EXECUTIONREQUEST']._serialized_start=336
  _globals['_EXECUTIONREQUEST']._serialized_end=539
  _globals['_AGENTHELLO']._serialized_start=541
  _globals['_AGENTHELLO']._serialized_end=572
  _globals['_GOODBYE']._serialized_start=574
  _globals['_GOODBYE']._serialized_end=583
  _globals['_UPDATEWORKLOAD']._serialized_start=585
  _globals['_UPDATEWORKLOAD']._serialized_end=701
  _globals['_ADDEDWORKLOAD']._serialized_start=704
  _globals['_ADDEDWORKLOAD']._serialized_end=1053
  _globals['_ADDEDWORKLOAD_DEPENDENCIESENTRY']._serialized_start=978
  _globals['_ADDEDWORKLOAD_DEPENDENCIESENTRY']._serialized_end=1053
  _globals['_DELETEDWORKLOAD']._serialized_start=1056
  _globals['_DELETEDWORKLOAD']._serialized_end=1230
  _globals['_DELETEDWORKLOAD_DEPENDENCIESENTRY']._serialized_start=978
  _globals['_DELETEDWORKLOAD_DEPENDENCIESENTRY']._serialized_end=1053
  _globals['_WORKLOADSTATE']._serialized_start=1232
  _globals['_WORKLOADSTATE']._serialized_end=1337
  _globals['_UPDATEWORKLOADSTATE']._serialized_start=1339
  _globals['_UPDATEWORKLOADSTATE']._serialized_end=1408
  _globals['_COMPLETESTATE']._serialized_start=1411
  _globals['_COMPLETESTATE']._serialized_end=1569
  _globals['_REQUESTCOMPLETESTATE']._serialized_start=1571
  _globals['_REQUESTCOMPLETESTATE']._serialized_end=1631
  _globals['_UPDATESTATEREQUEST']._serialized_start=1633
  _globals['_UPDATESTATEREQUEST']._serialized_end=1715
  _globals['_STATE']._serialized_start=1718
  _globals['_STATE']._serialized_end=2053
  _globals['_STATE_WORKLOADSENTRY']._serialized_start=1871
  _globals['_STATE_WORKLOADSENTRY']._serialized_end=1938
  _globals['_STATE_CONFIGSENTRY']._serialized_start=1940
  _globals['_STATE_CONFIGSENTRY']._serialized_end=1986
  _globals['_STATE_CRONJOBSENTRY']._serialized_start=1988
  _globals['_STATE_CRONJOBSENTRY']._serialized_end=2053
  _globals['_WORKLOAD']._serialized_start=2056
  _globals['_WORKLOAD']._serialized_end=2396
  _globals['_WORKLOAD_DEPENDENCIESENTRY']._serialized_start=978
  _globals['_WORKLOAD_DEPENDENCIESENTRY']._serialized_end=1053
  _globals['_TAG']._serialized_start=2398
  _globals['_TAG']._serialized_end=2431
  _globals['_ACCESSRIGHTS']._serialized_start=2433
  _globals['_ACCESSRIGHTS']._serialized_end=2530
  _globals['_ACCESSRIGHTSRULE']._serialized_start=2532
  _globals['_ACCESSRIGHTSRULE']._serialized_end=2629
  _globals['_CRONJOB']._serialized_start=2631
  _globals['_CRONJOB']._serialized_end=2695
  _globals['_INTERVAL']._serialized_start=2697
  _globals['_INTERVAL']._serialized_end=2756
  _globals['_AGENTCONNECTION']._serialized_start=3052
  _globals['_AGENTCONNECTION']._serialized_end=3145
  _globals['_CLICONNECTION']._serialized_start=3147
  _globals['_CLICONNECTION']._serialized_end=3236
# @@protoc_insertion_point(module_scope)
