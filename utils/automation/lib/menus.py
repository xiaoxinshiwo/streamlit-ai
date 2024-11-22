from langchain_core.tools import BaseTool

from utils.automation.base_lib_class import BaseLibClass
from utils.automation.tools import get_clean_val


class OpenDashboardPrivatePage(BaseTool):
	name: str = "Tool to generate code to open open a private dashboard page"
	description: str = (
		"Use this Tool to generate code to open open a private dashboard page. "
		"Parameters: {'pageName': the name of the page to open, string type parameter}"
	)

	def _run(self, pageName):
		pageName = get_clean_val(pageName)
		return f"await Menus.openDashboardPrivatePage('{pageName}');"


class OpenPersonalizeDashboard(BaseTool):
	name: str = "Tool to generate code to open personalize the dashboard"
	description: str = (
		"Use this Tool to generate code to open open the personalization menu for the dashboard."
	)

	def _run(self):
		return "await Menus.openPersonalizeDashboard(page);"


class OpenSearchRequest(BaseTool):
	name: str = "Tool to generate code to open open the search request page"
	description: str = (
		"Use this Tool to generate code to open navigate to the search request page."
	)

	def _run(self):
		return "await Menus.openSearchRequest(page);"


class OpenManageSavedSearches(BaseTool):
	name: str = "Tool to generate code to open manage saved searches"
	description: str = (
		"Use this Tool to generate code to open open the Manage Saved Searches page."
	)

	def _run(self):
		return "await Menus.openManageSavedSearches(page);"


class OpenSearchProject(BaseTool):
	name: str = "Tool to generate code to open search for projects"
	description: str = (
		"Use this Tool to generate code to open navigate to the search project page."
	)

	def _run(self):
		return "await Menus.openSearchProject(page);"


class OpenCreateRequest(BaseTool):
	name: str = "Tool to generate code to open Create Request page"
	description: str = (
		"Use this Tool to generate code to open navigate to the Create Request page."
	)

	def _run(self):
		return "await Menus.openCreateRequest(page);"


class OpenCreateProjectIssue(BaseTool):
	name: str = "Tool to generate code to open create a project issue"
	description: str = (
		"Use this Tool to generate code to open navigate to the Submit Project Issue page."
	)

	def _run(self):
		return "await Menus.openCreateProjectIssue(page);"


class OpenCreateRegion(BaseTool):
	name: str = "Tool to generate code to open create a region"
	description: str = (
		"Use this Tool to generate code to open navigate to the Create Region page in the Admin Console."
	)

	def _run(self):
		return "await Menus.openCreateRegion(page);"


class OpenCreateProposal(BaseTool):
	name: str = "Tool to generate code to open create a proposal"
	description: str = (
		"Use this Tool to generate code to open navigate to the Create Proposal page."
	)

	def _run(self):
		return "await Menus.openCreateProposal(page);"


class OpenCreateResourcepool(BaseTool):
	name: str = "Tool to generate code to open create a resource pool"
	description: str = (
		"Use this Tool to generate code to open navigate to the Create Resource Pool page."
	)

	def _run(self):
		return "await Menus.openCreateResourcepool(page);"


class OpenCreateRole(BaseTool):
	name: str = "Tool to generate code to open create a role"
	description: str = (
		"Use this Tool to generate code to open navigate to the Create Role page."
	)

	def _run(self):
		return "await Menus.openCreateRole(page);"


class OpenCreateBilling(BaseTool):
	name: str = "Tool to generate code to open create billing"
	description: str = (
		"Use this Tool to generate code to open navigate to the Create Billing page."
	)

	def _run(self):
		return "await Menus.openCreateBilling(page);"


class OpenCreateAdminConsoleRole(BaseTool):
	name: str = "Tool to generate code to open create an admin console role"
	description: str = (
		"Use this Tool to generate code to open navigate to the Create Admin Console Role page."
	)

	def _run(self):
		return "await Menus.openCreateAdminConsoleRole(page);"


class OpenCreateAdminConsoleUser(BaseTool):
	name: str = "Tool to generate code to open create an admin console user"
	description: str = (
		"Use this Tool to generate code to open navigate to the Create Admin Console User page."
	)

	def _run(self):
		return "await Menus.openCreateAdminConsoleUser(page);"


class OpenEditAdminConsoleUser(BaseTool):
	name: str = "Tool to generate code to open edit an admin console user"
	description: str = (
		"Use this Tool to generate code to open navigate to the Edit Admin Console User page."
	)

	def _run(self):
		return "await Menus.openEditAdminConsoleUser(page);"


class OpenManageUsers(BaseTool):
	name: str = "Tool to generate code to open manage users"
	description: str = (
		"Use this Tool to generate code to open navigate to the Manage Users page in the Admin Console."
	)

	def _run(self):
		return "await Menus.openManageUsers(page);"


class OpenManageRoles(BaseTool):
	name: str = "Tool to generate code to open manage roles"
	description: str = (
		"Use this Tool to generate code to open navigate to the Manage Roles page in the Admin Console."
	)

	def _run(self):
		return "await Menus.openManageRoles(page);"


class OpenManageRegions(BaseTool):
	name: str = "Tool to generate code to open manage regions"
	description: str = (
		"Use this Tool to generate code to open navigate to the Manage Regions page in the Admin Console."
	)

	def _run(self):
		return "await Menus.openManageRegions(page);"


class OpenManageProjects(BaseTool):
	name: str = "Tool to generate code to open manage projects"
	description: str = (
		"Use this Tool to generate code to open navigate to the Manage Projects page."
	)

	def _run(self):
		return "await Menus.openManageProjects(page);"


class OpenViewBilling(BaseTool):
	name: str = "Tool to generate code to open view billing details"
	description: str = (
		"Use this Tool to generate code to open navigate to the View Billing Details page."
	)

	def _run(self):
		return "await Menus.openViewBilling(page);"


class OpenViewResourcePool(BaseTool):
	name: str = "Tool to generate code to open view resource pools"
	description: str = (
		"Use this Tool to generate code to open navigate to the View Resource Pools page."
	)

	def _run(self):
		return "await Menus.openViewResourcePool(page);"


class OpenViewProposal(BaseTool):
	name: str = "Tool to generate code to open view proposals"
	description: str = (
		"Use this Tool to generate code to open navigate to the View Proposals page."
	)

	def _run(self):
		return "await Menus.openViewProposal(page);"


class OpenViewSubscription(BaseTool):
	name: str = "Tool to generate code to open view subscription details"
	description: str = (
		"Use this Tool to generate code to open navigate to the View Subscription Details page."
	)

	def _run(self):
		return "await Menus.openViewSubscription(page);"


class OpenViewUsage(BaseTool):
	name: str = "Tool to generate code to open view usage details"
	description: str = (
		"Use this Tool to generate code to open navigate to the View Usage page."
	)

	def _run(self):
		return "await Menus.openViewUsage(page);"


class OpenManageNotifications(BaseTool):
	name: str = "Tool to generate code to open manage notifications"
	description: str = (
		"Use this Tool to generate code to open navigate to the Manage Notifications page."
	)

	def _run(self):
		return "await Menus.openManageNotifications(page);"


class OpenManageAuditLogs(BaseTool):
	name: str = "Tool to generate code to open manage audit logs"
	description: str = (
		"Use this Tool to generate code to open navigate to the Manage Audit Logs page."
	)

	def _run(self):
		return "await Menus.openManageAuditLogs(page);"


class OpenManageSecurity(BaseTool):
	name: str = "Tool to generate code to open manage security settings"
	description: str = (
		"Use this Tool to generate code to open navigate to the Manage Security Settings page."
	)

	def _run(self):
		return "await Menus.openManageSecurity(page);"


class OpenManageIdentity(BaseTool):
	name: str = "Tool to generate code to open manage identity settings"
	description: str = (
		"Use this Tool to generate code to open navigate to the Manage Identity Settings page."
	)

	def _run(self):
		return "await Menus.openManageIdentity(page);"


class OpenManageDomains(BaseTool):
	name: str = "Tool to generate code to open manage domains"
	description: str = (
		"Use this Tool to generate code to open navigate to the Manage Domains page."
	)

	def _run(self):
		return "await Menus.openManageDomains(page);"


class OpenManageAccountSettings(BaseTool):
	name: str = "Tool to generate code to open manage account settings"
	description: str = (
		"Use this Tool to generate code to open navigate to the Manage Account Settings page."
	)

	def _run(self):
		return "await Menus.openManageAccountSettings(page);"


class OpenCreateAPIKey(BaseTool):
	name: str = "Tool to generate code to open create an API key page"
	description: str = (
		"Use this Tool to generate code to open navigate to the Create API Key page."
	)

	def _run(self):
		return "await Menus.openCreateAPIKey(page);"


class OpenManageAPIKeys(BaseTool):
	name: str = "Tool to generate code to open manage API keys"
	description: str = (
		"Use this Tool to generate code to open navigate to the Manage API Keys page."
	)

	def _run(self):
		return "await Menus.openManageAPIKeys(page);"


class OpenViewReports(BaseTool):
	name: str = "Tool to generate code to open view reports"
	description: str = (
		"Use this Tool to generate code to open navigate to the View Reports page."
	)

	def _run(self):
		return "await Menus.openViewReports(page);"


class Menus(BaseLibClass):
	@staticmethod
	def get_tools():
		return [
			OpenDashboardPrivatePage(),
			OpenPersonalizeDashboard(),
			OpenSearchRequest(),
			OpenManageSavedSearches(),
			OpenSearchProject(),
			OpenCreateRequest(),
			OpenCreateProjectIssue(),
			OpenCreateRegion(),
			OpenCreateProposal(),
			OpenCreateResourcepool(),
			OpenCreateRole(),
			OpenCreateBilling(),
			# OpenCreateAdminConsoleRole(),
			# OpenCreateAdminConsoleUser(),
			# OpenEditAdminConsoleUser(),
			# OpenManageUsers(),
			# OpenManageRoles(),
			# OpenManageRegions(),
			# OpenManageProjects(),
			# OpenViewBilling(),
			# OpenViewResourcePool(),
			# OpenViewProposal(),
			# OpenViewSubscription(),
			# OpenViewUsage(),
			# OpenManageNotifications(),
			# OpenManageAuditLogs(),
			# OpenManageSecurity(),
			# OpenManageIdentity(),
			# OpenManageDomains(),
			OpenManageAccountSettings(),
			OpenCreateAPIKey(),
			OpenManageAPIKeys(),
			OpenViewReports(),
		]
