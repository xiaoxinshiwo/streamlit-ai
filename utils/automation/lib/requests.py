from langchain_core.tools import BaseTool

from utils.automation.base_lib_class import BaseLibClass
from utils.automation.tools import get_clean_val


class SaveRequest(BaseTool):
	name: str = "Tool to generate code to save a request"
	description: str = (
		'Use this tool when you are asked to save a request, need to import dependency: import {Requests} from "@lib/Requests";'
	)

	def _run(self):
		return "await Requests.saveRequest(page);"


class SubmitRequest(BaseTool):
	name: str = "Tool to generate code to submit a request"
	description: str = (
		'Use this tool when you are asked to submit a request, need to import dependency: import {Requests} from "@lib/Requests";'
	)

	def _run(self):
		return "await Requests.submitRequest(page);"


class CreateRequest(BaseTool):
	name: str = "Tool to generate code to create a request of a specific type"
	description: str = (
		'Use this tool when you are asked to create a request  of a specific type, need to import dependency: import {Requests} from "@lib/Requests";'
		"'request_type': the type of a request, string type parameter"
	)

	def _run(self, request_type):
		request_type = get_clean_val(request_type)
		return f'await Requests.openCreateRequestPage(page, "{request_type}");'


class DeleteRequest(BaseTool):
	name: str = "Tool to generate code to delete a request"
	description: str = (
		'Use this tool when you are asked to delete a request, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'request_id': the id of a request, number type parameter}"
	)

	def _run(self, request_id):
		request_id = get_clean_val(request_id)
		return f"await Requests.deleteRequest(page, {request_id});"


class AddNote(BaseTool):
	name: str = "Tool to generate code to add note to a request"
	description: str = (
		'Use this tool when you are asked to add note to a request, need to import dependency: import {Requests} from "@lib/Requests";'
		"'note': the content, string type parameter"
	)

	def _run(self, note):
		note = get_clean_val(note)
		return f"await Requests.addNote(page, '{note}');"


class ClickWorkflowAction(BaseTool):
	name: str = "Tool to generate code to click workflow button"
	description: str = (
		'Use this tool when you are asked to click workflow button, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'action':  the name of workflow button, string type parameter}"
	)

	def _run(self, action):
		action = get_clean_val(action)
		return f"await Requests.clickWfAction(page, '{action}');"



class UpdateRequest(BaseTool):
	name: str = "Tool to generate code for updating a request"
	description: str = (
		'Use this tool when you are asked to update a request, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'requestFields': an array of fields to update}"
	)

	def _run(self, requestFields):
		requestFields = get_clean_val(requestFields)
		return f"await Requests.UpdateRequest(page, {requestFields});"


class ContinueWfConfirm(BaseTool):
	name: str = "Tool to generate code to confirm workflow continuation"
	description: str = (
		'Use this tool when you are asked to continue workflow confirmation, need to import dependency: import {Requests} from "@lib/Requests";'
	)

	def _run(self):
		return f"await Requests.continueWfConfirm(page);"


class DeleteRequests(BaseTool):
	name: str = "Tool to delete multiple requests"
	description: str = (
		'Use this tool when you are asked to delete multiple requests, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'requestIds': an array of request IDs}"
	)

	def _run(self, requestIds):
		requestIds = get_clean_val(requestIds)
		return f"await Requests.deleteRequests(page, {requestIds});"


# class DeleteRequestOnRequestDetailPage(BaseTool):
# 	name: str = "Tool to generate code to delete request on request detail page"
# 	description: str = (
# 		'Use this tool when you are asked to delete request on request detail page, need to import dependency: import {Requests} from "@lib/Requests";'
# 	)
#
# 	def _run(self):
# 		return "await Requests.deleteRequestOnRequestDetailPage(page);"


class GetRequestStatus(BaseTool):
	name: str = "Tool to get the status of a request"
	description: str = (
		'Use this tool when you are asked to fetch the status of a request, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'requestId': ID of the request}"
	)

	def _run(self, requestId):
		requestId = get_clean_val(requestId)
		return f"await Requests.getRequestStatus(page, {requestId});"


class GetRequestFields(BaseTool):
	name: str = "Tool to fetch the fields of a request"
	description: str = (
		'Use this tool when you are asked to fetch the fields of a request, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'requestId': ID of the request}"
	)

	def _run(self, requestId):
		requestId = get_clean_val(requestId)
		return f"await Requests.getRequestFields(page, {requestId});"


class OpenRequestDetailsPage(BaseTool):
	name: str = "Tool to open the details page of a request"
	description: str = (
		'Use this tool when you are asked to navigate to the request details page, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'requestId': ID of the request}"
	)

	def _run(self, requestId):
		requestId = get_clean_val(requestId)
		return f"await Requests.openRequestDetailsPage(page, {requestId});"


class CancelRequest(BaseTool):
	name: str = "Tool to cancel a request"
	description: str = (
		'Use this tool when you are asked to cancel a request, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'requestId': ID of the request, 'cancelReason': reason for cancellation}"
	)

	def _run(self, requestId, cancelReason):
		requestId = get_clean_val(requestId)
		cancelReason = get_clean_val(cancelReason)
		return f"await Requests.cancelRequest(page, {requestId}, {cancelReason});"


class ApproveRequest(BaseTool):
	name: str = "Tool to approve a request"
	description: str = (
		'Use this tool when you are asked to approve a request, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'requestId': ID of the request, 'approveOptions': additional options}"
	)

	def _run(self, requestId, approveOptions=None):
		requestId = get_clean_val(requestId)
		approveOptions = get_clean_val(approveOptions)
		return f"await Requests.approveRequest(page, {requestId}, {approveOptions});"


class RejectRequest(BaseTool):
	name: str = "Tool to reject a request"
	description: str = (
		'Use this tool when you are asked to reject a request, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'requestId': ID of the request, 'rejectReason': reason for rejection}"
	)

	def _run(self, requestId, rejectReason):
		requestId = get_clean_val(requestId)
		rejectReason = get_clean_val(rejectReason)
		return f"await Requests.rejectRequest(page, {requestId}, '{rejectReason}');"


class SearchRequests(BaseTool):
	name: str = "Tool to search for requests"
	description: str = (
		'Use this tool when you are asked to search for requests, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'searchCriteria': criteria to search for requests}"
	)

	def _run(self, searchCriteria):
		searchCriteria = get_clean_val(searchCriteria)
		return f"await Requests.searchRequests(page, {searchCriteria});"


class ArchiveRequest(BaseTool):
	name: str = "Tool to archive a request"
	description: str = (
		'Use this tool when you are asked to archive a request, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'requestId': ID of the request}"
	)

	def _run(self, requestId):
		requestId = get_clean_val(requestId)
		return f"await Requests.archiveRequest(page, {requestId});"


class AddAttachmentToRequest(BaseTool):
	name: str = "Tool to add attachment to a request"
	description: str = (
		'Use this tool when you need to add an attachment to a request, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'filePath': file to attach, 'refRequestType': optional request type, 'addRefElementSelector': optional reference element selector}"
	)

	def _run(self, filePath, refRequestType=None, addRefElementSelector=None):
		filePath = get_clean_val(filePath)
		refRequestType = get_clean_val(refRequestType) if refRequestType else "Attachment"
		addRefElementSelector = get_clean_val(
			addRefElementSelector) if addRefElementSelector else "id=IMAGE_EC_REQUEST_REFERENCES"
		return f"await Requests.addAttachmentToRequest(page, {filePath}, {refRequestType}, {addRefElementSelector});"


class AddAttachmentToRequestFromRequestTypeFieldsBlock(BaseTool):
	name: str = "Tool to add attachment from request type fields block"
	description: str = (
		'Use this tool when you need to add an attachment from the request type fields block, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'filePath': file to attach, 'description': optional description}"
	)

	def _run(self, filePath, description=None):
		filePath = get_clean_val(filePath)
		description = get_clean_val(description) if description else ''
		return f"await Requests.addAttachmentToRequestFromRequestTypeFieldsBlock(page, {filePath}, {description});"


class DeleteAttachmentOnRequestFromRequestTypeFieldsBlock(BaseTool):
	name: str = "Tool to delete attachment from request type fields block"
	description: str = (
		'Use this tool when you need to delete an attachment from the request type fields block, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'page': the page object}"
	)

	def _run(self):
		return f"await Requests.deleteAttachmentOnRequestFromRequestTypeFieldsBlock(page);"


class ChooseColumnsFromLeft(BaseTool):
	name: str = "Tool to choose columns from left list"
	description: str = (
		'Use this tool when you need to choose columns from the left list, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'chooseLeftArray': array of column names to choose}"
	)

	def _run(self, chooseLeftArray):
		chooseLeftArray = get_clean_val(chooseLeftArray)
		return f"await Requests.chooseColumnsFromLeft(page, {chooseLeftArray});"


class ProceedWorkFlow(BaseTool):
	name: str = "Tool to proceed with the workflow"
	description: str = (
		'Use this tool when you need to proceed with the workflow, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'workflowBtnSelector': button selector, 'nextStageWorkFlowStatus': expected next stage workflow status}"
	)

	def _run(self, workflowBtnSelector, nextStageWorkFlowStatus):
		return f"await Requests.proceedWorkFlow(page, {workflowBtnSelector}, {nextStageWorkFlowStatus});"


class AssertStatusCorrect(BaseTool):
	name: str = "Tool to assert the status is correct"
	description: str = (
		'Use this tool when you need to assert the status of the request is correct, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'statusSelector': status selector, 'expectStatus': expected status}"
	)

	def _run(self, statusSelector, expectStatus):
		return f"await Requests.assertStatusCorrect(page, {statusSelector}, {expectStatus});"


class ValidateNote(BaseTool):
	name: str = "Tool to validate the note in the request"
	description: str = (
		'Use this tool when you need to validate the note in the request, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'noteValidationModel': note validation object, 'rowNumber': optional row number to validate}"
	)

	def _run(self, noteValidationModel, rowNumber=1):
		return f"await Requests.validateNote(page, {noteValidationModel}, {rowNumber});"


class FillTableFields(BaseTool):
	name: str = "Tool to fill the table fields"
	description: str = (
		'Use this tool when you need to fill table fields, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'goToView': optional flag to go to view after filling the table}"
	)

	def _run(self, goToView=True):
		return f"await Requests.fillTableFields(page, {goToView});"


class AddLink(BaseTool):
	name: str = "Tool to add a link to the request"
	description: str = (
		'Use this tool when you need to add a link to the request, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'addLinkBtnSelector': button selector to add link, 'link': the link to add}"
	)

	def _run(self, addLinkBtnSelector, link):
		return f"await Requests.addLink(page, {addLinkBtnSelector}, {link});"


class AddPassword(BaseTool):
	name: str = "Tool to add a password to the request"
	description: str = (
		'Use this tool when you need to add a password to the request, need to import dependency: import {Requests} from "@lib/Requests";'
		"{'addPasswordBtnSelector': button selector to add password, 'password': the password to add}"
	)

	def _run(self, addPasswordBtnSelector, password):
		return f"await Requests.addPassword(page, {addPasswordBtnSelector}, {password});"


class AddResourceViaAssignedToField(BaseTool):
	name: str = "Tool to add resource via Assigned To field"
	description: str = (
		'Use this tool when you need to add a resource via the "Assigned To" field, '
		'import dependency: import {Requests} from "@lib/Requests"; '
		"{'firstName': resource first name, 'lastName': resource last name, 'searchResultRowNumber': row number to select, 'isNeedSave': flag to save the request}"
	)

	def _run(self, firstName, lastName, searchResultRowNumber=1, isNeedSave=True):
		firstName = get_clean_val(firstName)
		lastName = get_clean_val(lastName)
		return f"await Requests.addResourceViaAssignedToField(page, {firstName}, {lastName}, {searchResultRowNumber}, {isNeedSave});"


class AddResourceViaAutoUserIdField(BaseTool):
	name: str = "Tool to add resource via Auto User ID field"
	description: str = (
		'Use this tool when you need to add a resource via the "Auto User ID" field, '
		'import dependency: import {Requests} from "@lib/Requests"; '
		"{'firstName': resource first name, 'lastName': resource last name, 'searchResultRowNumber': row number to select, 'isNeedSave': flag to save the request}"
	)

	def _run(self, firstName, lastName, searchResultRowNumber=1, isNeedSave=True):
		firstName = get_clean_val(firstName)
		lastName = get_clean_val(lastName)
		return f"await Requests.addResourceViaAutoUserIdField(page, {firstName}, {lastName}, {searchResultRowNumber}, {isNeedSave});"


class AddResourceViaAutoUserNameField(BaseTool):
	name: str = "Tool to add resource via Auto User Name field"
	description: str = (
		'Use this tool when you need to add a resource via the "Auto User Name" field, '
		'import dependency: import {Requests} from "@lib/Requests"; '
		"{'firstName': resource first name, 'lastName': resource last name, 'searchResultRowNumber': row number to select, 'isNeedSave': flag to save the request}"
	)

	def _run(self, firstName, lastName, searchResultRowNumber=1, isNeedSave=True):
		firstName = get_clean_val(firstName)
		lastName = get_clean_val(lastName)
		return f"await Requests.addResourceViaAutoUserNameField(page, {firstName}, {lastName}, {searchResultRowNumber}, {isNeedSave});"


class CheckIsResourceExists(BaseTool):
	name: str = "Tool to check if a resource exists"
	description: str = (
		'Use this tool to check if a specific resource already exists, '
		'import dependency: import {Requests} from "@lib/Requests"; '
		"{'firstName': resource first name, 'lastName': resource last name}"
	)

	def _run(self, firstName, lastName):
		firstName = get_clean_val(firstName)
		lastName = get_clean_val(lastName)
		return f"await Requests.checkIsResourceDoesExist(page, {firstName}, {lastName});"


class AddResource(BaseTool):
	name: str = "Tool to add resource"
	description: str = (
		'Use this tool to add a resource, '
		'import dependency: import {Requests} from "@lib/Requests"; '
		"{'firstName': resource first name, 'lastName': resource last name, 'searchResultRowNumber': row number to select}"
	)

	def _run(self, firstName, lastName, searchResultRowNumber=1):
		firstName = get_clean_val(firstName)
		lastName = get_clean_val(lastName)
		return f"await Requests.addResource(page, {firstName}, {lastName}, {searchResultRowNumber});"


class IsResourceExists(BaseTool):
	name: str = "Tool to verify if resource exists"
	description: str = (
		'Use this tool to verify if a resource exists, '
		'import dependency: import {Requests} from "@lib/Requests"; '
		"{'firstName': resource first name, 'lastName': resource last name, 'rowNumber': optional row number to check}"
	)

	def _run(self, firstName, lastName, rowNumber=None):
		firstName = get_clean_val(firstName)
		lastName = get_clean_val(lastName)
		rowNumber = get_clean_val(rowNumber)
		return f"await Requests.isResourceDoesExist(page, {firstName}, {lastName}, {rowNumber});"


class ValidateAddedResource(BaseTool):
	name: str = "Tool to validate the added resource"
	description: str = (
		'Use this tool to validate if the resource fields are correctly populated, '
		'import dependency: import {Requests} from "@lib/Requests"; '
		"{'requestResourceFill': resource data model, 'rowNumber': row number to validate}"
	)

	def _run(self, requestResourceFill, rowNumber=None):
		requestResourceFill = get_clean_val(requestResourceFill)
		rowNumber = get_clean_val(rowNumber)
		return f"await Requests.validateAddedResource(page, {requestResourceFill}, {rowNumber});"


class FillResourceContent(BaseTool):
	name: str = "Tool to fill resource content"
	description: str = (
		'Use this tool to fill in the resource content fields, '
		'import dependency: import {Requests} from "@lib/Requests"; '
		"{'contentModel': the resource data model, 'rowNumber': optional row number to fill}"
	)

	def _run(self, contentModel, rowNumber=1):
		contentModel = get_clean_val(contentModel)
		return f"await Requests.fillResourceContent(page, {contentModel}, {rowNumber});"


class VerifyResourceInfoWithRequestsFields(BaseTool):
	name: str = "Tool to verify resource info with request fields"
	description: str = (
		'Use this tool to verify resource overall info with request fields, '
		'import dependency: import {Requests} from "@lib/Requests"; '
	)

	def _run(self):
		return f"await Requests.verifyResourceOverallInfoWithRequestsFields(page);"


class DeleteResource(BaseTool):
	name: str = "Tool to delete a resource"
	description: str = (
		'Use this tool to delete a resource, '
		'import dependency: import {Requests} from "@lib/Requests"; '
		"{'rowNumber': row number to delete}"
	)

	def _run(self, rowNumber=1):
		rowNumber = get_clean_val(rowNumber)
		return f"await Requests.deleteResource(page, {rowNumber});"


class AddAttachment(BaseTool):
	name: str = "Tool to add an attachment"
	description: str = (
		'Use this tool to add an attachment to the request, '
		'import dependency: import {Requests} from "@lib/Requests"; '
		"{'addFileBtnSelector': selector for the add file button, 'filePath': file path to attach}"
	)

	def _run(self, addFileBtnSelector, filePath):
		addFileBtnSelector = get_clean_val(addFileBtnSelector)
		filePath = get_clean_val(filePath)
		return f"await Requests.addAttachment(page, {addFileBtnSelector}, {filePath});"


class SelectRequestsToMassEdit(BaseTool):
	name: str = "Tool to select requests for mass edit"
	description: str = (
		'Use this tool to select multiple requests for mass edit, '
		'import dependency: import {Requests} from "@lib/Requests"; '
		"{'requestIds': list of request IDs}"
	)

	def _run(self, requestIds):
		requestIds = get_clean_val(requestIds)
		return f"await Requests.selectRequestsToMassEdit(page, {requestIds});"


class SelectRequestsToDelete(BaseTool):
	name: str = "Tool to select requests for deletion"
	description: str = (
		'Use this tool to select multiple requests for deletion, '
		'import dependency: import {Requests} from "@lib/Requests"; '
		"{'requestIds': list of request IDs}"
	)

	def _run(self, requestIds):
		requestIds = get_clean_val(requestIds)
		return f"await Requests.selectRequestsToDelete(page, {requestIds});"


class Requests(BaseLibClass):
	@staticmethod
	def get_tools():
		return [
			SaveRequest(),
			SubmitRequest(),
			CreateRequest(),
			DeleteRequest(),
			AddNote(),
			ClickWorkflowAction(),
			UpdateRequest(),
			ContinueWfConfirm(),
			DeleteRequests(),
			# DeleteRequestOnRequestDetailPage(),
			GetRequestStatus(),
			GetRequestFields(),
			OpenRequestDetailsPage(),
			CancelRequest(),
			ApproveRequest(),
			RejectRequest(),
			SearchRequests(),
			ArchiveRequest(),
			# AddAttachmentToRequest(),
			# AddAttachmentToRequestFromRequestTypeFieldsBlock(),
			# DeleteAttachmentOnRequestFromRequestTypeFieldsBlock(),
			# ChooseColumnsFromLeft(),
			# ProceedWorkFlow(),
			# AssertStatusCorrect(),
			# ValidateNote(),
			# FillTableFields(),
			# AddLink(),
			# AddPassword(),
			# AddResourceViaAssignedToField(),
			# AddResourceViaAutoUserIdField(),
			# AddResourceViaAutoUserNameField(),
			# CheckIsResourceExists(),
			# AddResource(),
			# IsResourceExists(),
			# ValidateAddedResource(),
			# FillResourceContent(),
			# VerifyResourceInfoWithRequestsFields(),
			# DeleteResource(),
			# AddAttachment(),
			# SelectRequestsToMassEdit(),
			# SelectRequestsToDelete(),
		]
