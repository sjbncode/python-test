#!/usr/bin/python
#
# This script is intended to be run as a commit-msg script in a GIT
# repository and check the presence of JIRA ticket numbers in the log messages.
#
#    - NO_JIRA_TICKET_MESSAGE (an error message returned to the user when the
#      svn commit message doesn't contain a jira ticket);
#    - INVALID_JIRA_TICKET_MESSAGE (an error message returned to the user when
#      the svn commit message contains an invalid jira ticket);
#    - JIRA_XMLRPC (url of the JIRA XML-RPC server);
#    - JIRA_USER (name of the JIRA user who has permission to look up issues in
#      the JIRA server);
#    - JIRA_PASSWORD (password of the JIRA user described above);
 
import sys
import re
#import xmlrpclib
import xmlrpc.client
print(dir(xmlrpc.client))
xmlrpclib=xmlrpc.client

NO_JIRA_TICKET_MESSAGE = \
'No JIRA ticket present in the commit message. \
Please include the JIRA ticket enclosed in brackets: [ABC-789].'
INVALID_JIRA_TICKET_MESSAGE = \
'Proper JIRA ticket syntax was found, but none were valid tickets. \
Please check the tickets and try again.'
TOO_MANY_JIRA_TICKETS_MESSAGE = \
'Only 1 JIRA ticket is allowed per commit. Please commit only 1 change at a time.'
INVALID_ISSUE_TYPE_MESSAGE = \
'You may not commit against subtasks or task-splits. \
Please commit against the parent ticket.'
 
JIRA_XMLRPC = 'http://jira.local.genewiz.com/rpc/xmlrpc'
JIRA_USER = 'GitToJira'
JIRA_PASSWORD = '12345678'
JIRA_TICKET_PATTERN = re.compile(r'\[(\w+?-\d+?)\]')
FAULT_MSG_ISSUE_NOT_FOUND = 'com.atlassian.jira.rpc.exception.RemotePermissionException'
 
def check_message(message):
    tickets = JIRA_TICKET_PATTERN.findall(message)
 
    if not tickets:
        return NO_JIRA_TICKET_MESSAGE
 
    if len(tickets) > 1:
        return TOO_MANY_JIRA_TICKETS_MESSAGE
 
    ticket = tickets[0]
 
    try:
        issue = proxy.jira1.getIssue(auth, ticket)
    except(xmlrpclib.Fault, e):
        if e.faultString.find(FAULT_MSG_ISSUE_NOT_FOUND) >= 0:
            return INVALID_JIRA_TICKET_MESSAGE
        else:
            raise
 
    # Check if issue is subtask or task-split
    #if issue['type'] == '8' or issue['type'] == '5':
    #    return INVALID_ISSUE_TYPE_MESSAGE
        
    return None
    
	
proxy = xmlrpclib.ServerProxy(JIRA_XMLRPC)
 
try:
    auth = proxy.jira1.login(JIRA_USER, JIRA_PASSWORD)

except:
    print >> sys.stderr, 'Cannot connect to JIRA: ' + str(sys.exc_info()[1])
    sys.exit(2)
 
msg="[GCF-2685] confirmed with Cherry. we should always display the  field"
print(msg) 
#err_msg = check_message(msg)
err_msg='xxx'
print(err_msg)

print (sys.stderr, 'Error: %s\nCommit message:\n%s' % (err_msg, msg))
