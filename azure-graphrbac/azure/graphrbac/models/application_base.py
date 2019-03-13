# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApplicationBase(Model):
    """Active Directive Application common properties shared among GET, POST and
    PATCH.

    :param allow_guests_sign_in: A property on the application to indicate if
     the application accepts other IDPs or not or partially accepts.
    :type allow_guests_sign_in: bool
    :param allow_passthrough_users: Indicates that the application supports
     pass through users who have no presence in the resource tenant.
    :type allow_passthrough_users: bool
    :param app_logo_url: The url for the application logo image stored in a
     CDN.
    :type app_logo_url: str
    :param app_roles: The collection of application roles that an application
     may declare. These roles can be assigned to users, groups or service
     principals.
    :type app_roles: list[~azure.graphrbac.models.AppRole]
    :param app_permissions: The application permissions.
    :type app_permissions: list[str]
    :param available_to_other_tenants: Whether the application is available to
     other tenants.
    :type available_to_other_tenants: bool
    :param error_url: A URL provided by the author of the application to
     report errors when using the application.
    :type error_url: str
    :param group_membership_claims: Configures the groups claim issued in a
     user or OAuth 2.0 access token that the app expects.
    :type group_membership_claims: object
    :param homepage: The home page of the application.
    :type homepage: str
    :param informational_urls: urls with more informations of the application.
    :type informational_urls: ~azure.graphrbac.models.InformationalUrl
    :param is_device_only_auth_supported: Specifies whether this application
     supports device authentication without a user. The default is false.
    :type is_device_only_auth_supported: bool
    :param key_credentials: A collection of KeyCredential objects.
    :type key_credentials: list[~azure.graphrbac.models.KeyCredential]
    :param known_client_applications: Client applications that are tied to
     this resource application. Consent to any of the known client applications
     will result in implicit consent to the resource application through a
     combined consent dialog (showing the OAuth permission scopes required by
     the client and the resource).
    :type known_client_applications: list[str]
    :param logout_url: the url of the logout page
    :type logout_url: str
    :param oauth2_allow_implicit_flow: Whether to allow implicit grant flow
     for OAuth2
    :type oauth2_allow_implicit_flow: bool
    :param oauth2_allow_url_path_matching: Specifies whether during a token
     Request Azure AD will allow path matching of the redirect URI against the
     applications collection of replyURLs. The default is false.
    :type oauth2_allow_url_path_matching: bool
    :param oauth2_permissions: The collection of OAuth 2.0 permission scopes
     that the web API (resource) application exposes to client applications.
     These permission scopes may be granted to client applications during
     consent.
    :type oauth2_permissions: list[~azure.graphrbac.models.OAuth2Permission]
    :param oauth2_require_post_response: Specifies whether, as part of OAuth
     2.0 token requests, Azure AD will allow POST requests, as opposed to GET
     requests. The default is false, which specifies that only GET requests
     will be allowed.
    :type oauth2_require_post_response: bool
    :param org_restrictions: A list of tenants allowed to access application.
    :type org_restrictions: list[str]
    :param optional_claims:
    :type optional_claims: ~azure.graphrbac.models.OptionalClaims
    :param password_credentials: A collection of PasswordCredential objects
    :type password_credentials:
     list[~azure.graphrbac.models.PasswordCredential]
    :param pre_authorized_applications: list of pre-authorizaed applications.
    :type pre_authorized_applications:
     list[~azure.graphrbac.models.PreAuthorizedApplication]
    :param public_client: Specifies whether this application is a public
     client (such as an installed application running on a mobile device).
     Default is false.
    :type public_client: bool
    :param publisher_domain: Reliable domain which can be used to identify an
     application.
    :type publisher_domain: str
    :param reply_urls: A collection of reply URLs for the application.
    :type reply_urls: list[str]
    :param required_resource_access: Specifies resources that this application
     requires access to and the set of OAuth permission scopes and application
     roles that it needs under each of those resources. This pre-configuration
     of required resource access drives the consent experience.
    :type required_resource_access:
     list[~azure.graphrbac.models.RequiredResourceAccess]
    :param saml_metadata_url: The URL to the SAML metadata for the
     application.
    :type saml_metadata_url: str
    :param sign_in_audience: Audience for signing in to the application
     (AzureADMyOrganizatio, AzureADAllorganizations,
     AzureADAndMicrosofAccounts).
    :type sign_in_audience: str
    :param www_homepage: The primary Web page.
    :type www_homepage: str
    """

    _attribute_map = {
        'allow_guests_sign_in': {'key': 'allowGuestsSignIn', 'type': 'bool'},
        'allow_passthrough_users': {'key': 'allowPassthroughUsers', 'type': 'bool'},
        'app_logo_url': {'key': 'appLogoUrl', 'type': 'str'},
        'app_roles': {'key': 'appRoles', 'type': '[AppRole]'},
        'app_permissions': {'key': 'appPermissions', 'type': '[str]'},
        'available_to_other_tenants': {'key': 'availableToOtherTenants', 'type': 'bool'},
        'error_url': {'key': 'errorUrl', 'type': 'str'},
        'group_membership_claims': {'key': 'groupMembershipClaims', 'type': 'object'},
        'homepage': {'key': 'homepage', 'type': 'str'},
        'informational_urls': {'key': 'informationalUrls', 'type': 'InformationalUrl'},
        'is_device_only_auth_supported': {'key': 'isDeviceOnlyAuthSupported', 'type': 'bool'},
        'key_credentials': {'key': 'keyCredentials', 'type': '[KeyCredential]'},
        'known_client_applications': {'key': 'knownClientApplications', 'type': '[str]'},
        'logout_url': {'key': 'logoutUrl', 'type': 'str'},
        'oauth2_allow_implicit_flow': {'key': 'oauth2AllowImplicitFlow', 'type': 'bool'},
        'oauth2_allow_url_path_matching': {'key': 'oauth2AllowUrlPathMatching', 'type': 'bool'},
        'oauth2_permissions': {'key': 'oauth2Permissions', 'type': '[OAuth2Permission]'},
        'oauth2_require_post_response': {'key': 'oauth2RequirePostResponse', 'type': 'bool'},
        'org_restrictions': {'key': 'orgRestrictions', 'type': '[str]'},
        'optional_claims': {'key': 'optionalClaims', 'type': 'OptionalClaims'},
        'password_credentials': {'key': 'passwordCredentials', 'type': '[PasswordCredential]'},
        'pre_authorized_applications': {'key': 'preAuthorizedApplications', 'type': '[PreAuthorizedApplication]'},
        'public_client': {'key': 'publicClient', 'type': 'bool'},
        'publisher_domain': {'key': 'publisherDomain', 'type': 'str'},
        'reply_urls': {'key': 'replyUrls', 'type': '[str]'},
        'required_resource_access': {'key': 'requiredResourceAccess', 'type': '[RequiredResourceAccess]'},
        'saml_metadata_url': {'key': 'samlMetadataUrl', 'type': 'str'},
        'sign_in_audience': {'key': 'signInAudience', 'type': 'str'},
        'www_homepage': {'key': 'wwwHomepage', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationBase, self).__init__(**kwargs)
        self.allow_guests_sign_in = kwargs.get('allow_guests_sign_in', None)
        self.allow_passthrough_users = kwargs.get('allow_passthrough_users', None)
        self.app_logo_url = kwargs.get('app_logo_url', None)
        self.app_roles = kwargs.get('app_roles', None)
        self.app_permissions = kwargs.get('app_permissions', None)
        self.available_to_other_tenants = kwargs.get('available_to_other_tenants', None)
        self.error_url = kwargs.get('error_url', None)
        self.group_membership_claims = kwargs.get('group_membership_claims', None)
        self.homepage = kwargs.get('homepage', None)
        self.informational_urls = kwargs.get('informational_urls', None)
        self.is_device_only_auth_supported = kwargs.get('is_device_only_auth_supported', None)
        self.key_credentials = kwargs.get('key_credentials', None)
        self.known_client_applications = kwargs.get('known_client_applications', None)
        self.logout_url = kwargs.get('logout_url', None)
        self.oauth2_allow_implicit_flow = kwargs.get('oauth2_allow_implicit_flow', None)
        self.oauth2_allow_url_path_matching = kwargs.get('oauth2_allow_url_path_matching', None)
        self.oauth2_permissions = kwargs.get('oauth2_permissions', None)
        self.oauth2_require_post_response = kwargs.get('oauth2_require_post_response', None)
        self.org_restrictions = kwargs.get('org_restrictions', None)
        self.optional_claims = kwargs.get('optional_claims', None)
        self.password_credentials = kwargs.get('password_credentials', None)
        self.pre_authorized_applications = kwargs.get('pre_authorized_applications', None)
        self.public_client = kwargs.get('public_client', None)
        self.publisher_domain = kwargs.get('publisher_domain', None)
        self.reply_urls = kwargs.get('reply_urls', None)
        self.required_resource_access = kwargs.get('required_resource_access', None)
        self.saml_metadata_url = kwargs.get('saml_metadata_url', None)
        self.sign_in_audience = kwargs.get('sign_in_audience', None)
        self.www_homepage = kwargs.get('www_homepage', None)
