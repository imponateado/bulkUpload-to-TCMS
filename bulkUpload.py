import os
import sys
from tcms_api import TCMS
import base64

url = 
usrnm = sys.argv[1]
passwd = sys.argv[2]
exec_run_id = sys.argv[3]
image_directory = sys.argv[4]

api = TCMS(url, usrnm, passwd).exec

for filename in os.listdir(image_directory):
    image_file_path = os.path.join(image_directory, filename)
    if os.path.isfile(image_file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        with open(image_file_path, 'rb') as image_file:
             encoded_content = base64.b64encode(image_file.read()).decode('utf-8')
             try:
                 fileUploadResponse = api.User.add_attachment(image_file_path, encoded_content)
                 print(f"Possível variável guardando link para endereço da imagem no servidor: {fileUploadResponse}")
             except Exception as e:
                 print(f"Um erro ocorreu: {e}")
             commentAdditionResponse = api.TestExecution.add_comment(exec_run_id, f'![{fileUploadResponse['filename']}]({fileUploadResponse['url']})')
             print(f"Possível variável guardando status da adição do comentário na test execution: {commentAdditionResponse}")

'''
o pacote tcms-api é necessário para o funcionamento deste script

procedures atualmente suportadas pelo tcms da brbcard (data limite 28/08/2024):
Attachment.remove_attachment
Auth.login
Auth.logout
Bug.add_tag
Bug.details
Bug.filter
Bug.remove
Bug.remove_tag
Bug.report
Build.create
Build.filter
Build.update
Category.create
Category.filter
Classification.create
Classification.filter
Component.create
Component.filter
Component.update
Environment.add_property
Environment.properties
Environment.remove_property
KiwiTCMS.version
Markdown.render
PlanType.create
PlanType.filter
Priority.filter
Product.create
Product.filter
Tag.filter
TestCase.add_attachment
TestCase.add_comment
TestCase.add_component
TestCase.add_notification_cc
TestCase.add_property
TestCase.add_tag
TestCase.comments
TestCase.create
TestCase.filter
TestCase.get_notification_cc
TestCase.history
TestCase.list_attachments
TestCase.properties
TestCase.remove
TestCase.remove_comment
TestCase.remove_component
TestCase.remove_notification_cc
TestCase.remove_property
TestCase.remove_tag
TestCase.sortkeys
TestCase.update
TestCaseStatus.filter
TestExecution.add_comment
TestExecution.add_link
TestExecution.filter
TestExecution.get_comments
TestExecution.get_links
TestExecution.history
TestExecution.properties
TestExecution.remove_comment
TestExecution.remove_link
TestExecution.update
TestExecutionStatus.filter
TestPlan.add_attachment
TestPlan.add_attachment
TestPlan.add_case
TestPlan.add_tag
TestPlan.create
TestPlan.filter
TestPlan.list_attachments
TestPlan.remove_case
TestPlan.remove_tag
TestPlan.create
TestPlan.filter
TestPlan.list_attachments
TestPlan.remove_case
TestPlan.remove_tag
TestPlan.tree
TestPlan.remove_case
TestPlan.remove_tag
TestPlan.tree
TestPlan.remove_tag
TestPlan.tree
TestPlan.update
TestPlan.update_case_order
TestPlan.tree
TestPlan.update
TestPlan.update_case_order
TestRun.add_case
TestPlan.update
TestPlan.update_case_order
TestRun.add_case
TestPlan.update_case_order
TestRun.add_case
TestRun.add_cc
TestRun.add_case
TestRun.add_cc
TestRun.add_cc
TestRun.add_tag
TestRun.add_tag
TestRun.create
TestRun.filter
TestRun.get_cases
TestRun.filter
TestRun.get_cases
TestRun.properties
TestRun.remove_case
TestRun.remove_cc
TestRun.remove_tag
TestRun.update
Testing.breakdown
Testing.execution_trends
Testing.breakdown
Testing.execution_trends
Testing.execution_trends
Testing.individual_test_case_health
Testing.status_matrix
Testing.test_case_health
User.add_attachment
User.filter
User.join_group
User.update
Version.create
Version.filter
system.listMethods
system.methodHelp
system.methodSignature
system.multicall

código usado para listá-los:
import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://tcms.brbcard.com.br/xml-rpc/')

methods = server.system.listMethods()

for method in methods:
    print(method)
'''
