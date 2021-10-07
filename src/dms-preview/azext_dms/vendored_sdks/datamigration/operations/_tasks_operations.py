# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class TasksOperations(object):
    """TasksOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.datamigration.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list(
        self,
        group_name,  # type: str
        service_name,  # type: str
        project_name,  # type: str
        task_type=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.TaskList"]
        """Get tasks in a service.

        The services resource is the top-level resource that represents the Database Migration Service.
        This method returns a list of tasks owned by a service resource. Some tasks may have a status
        of Unknown, which indicates that an error occurred while querying the status of that task.

        :param group_name: Name of the resource group.
        :type group_name: str
        :param service_name: Name of the service.
        :type service_name: str
        :param project_name: Name of the project.
        :type project_name: str
        :param task_type: Filter tasks by task type.
        :type task_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either TaskList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.datamigration.models.TaskList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.TaskList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-07-15-preview"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'groupName': self._serialize.url("group_name", group_name, 'str'),
                    'serviceName': self._serialize.url("service_name", service_name, 'str'),
                    'projectName': self._serialize.url("project_name", project_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
                if task_type is not None:
                    query_parameters['taskType'] = self._serialize.query("task_type", task_type, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('TaskList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize.failsafe_deserialize(_models.ApiError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks'}  # type: ignore

    def create_or_update(
        self,
        group_name,  # type: str
        service_name,  # type: str
        project_name,  # type: str
        task_name,  # type: str
        parameters,  # type: "_models.ProjectTask"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ProjectTask"
        """Create or update task.

        The tasks resource is a nested, proxy-only resource representing work performed by a DMS
        instance. The PUT method creates a new task or updates an existing one, although since tasks
        have no mutable custom properties, there is little reason to update an existing one.

        :param group_name: Name of the resource group.
        :type group_name: str
        :param service_name: Name of the service.
        :type service_name: str
        :param project_name: Name of the project.
        :type project_name: str
        :param task_name: Name of the Task.
        :type task_name: str
        :param parameters: Information about the task.
        :type parameters: ~azure.mgmt.datamigration.models.ProjectTask
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProjectTask, or the result of cls(response)
        :rtype: ~azure.mgmt.datamigration.models.ProjectTask
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ProjectTask"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-07-15-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_or_update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'taskName': self._serialize.url("task_name", task_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'ProjectTask')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('ProjectTask', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('ProjectTask', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName}'}  # type: ignore

    def get(
        self,
        group_name,  # type: str
        service_name,  # type: str
        project_name,  # type: str
        task_name,  # type: str
        expand=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ProjectTask"
        """Get task information.

        The tasks resource is a nested, proxy-only resource representing work performed by a DMS
        instance. The GET method retrieves information about a task.

        :param group_name: Name of the resource group.
        :type group_name: str
        :param service_name: Name of the service.
        :type service_name: str
        :param project_name: Name of the project.
        :type project_name: str
        :param task_name: Name of the Task.
        :type task_name: str
        :param expand: Expand the response.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProjectTask, or the result of cls(response)
        :rtype: ~azure.mgmt.datamigration.models.ProjectTask
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ProjectTask"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-07-15-preview"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'taskName': self._serialize.url("task_name", task_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ProjectTask', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName}'}  # type: ignore

    def delete(
        self,
        group_name,  # type: str
        service_name,  # type: str
        project_name,  # type: str
        task_name,  # type: str
        delete_running_tasks=None,  # type: Optional[bool]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete task.

        The tasks resource is a nested, proxy-only resource representing work performed by a DMS
        instance. The DELETE method deletes a task, canceling it first if it's running.

        :param group_name: Name of the resource group.
        :type group_name: str
        :param service_name: Name of the service.
        :type service_name: str
        :param project_name: Name of the project.
        :type project_name: str
        :param task_name: Name of the Task.
        :type task_name: str
        :param delete_running_tasks: Delete the resource even if it contains running tasks.
        :type delete_running_tasks: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-07-15-preview"
        accept = "application/json"

        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'taskName': self._serialize.url("task_name", task_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')
        if delete_running_tasks is not None:
            query_parameters['deleteRunningTasks'] = self._serialize.query("delete_running_tasks", delete_running_tasks, 'bool')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName}'}  # type: ignore

    def update(
        self,
        group_name,  # type: str
        service_name,  # type: str
        project_name,  # type: str
        task_name,  # type: str
        parameters,  # type: "_models.ProjectTask"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ProjectTask"
        """Create or update task.

        The tasks resource is a nested, proxy-only resource representing work performed by a DMS
        instance. The PATCH method updates an existing task, but since tasks have no mutable custom
        properties, there is little reason to do so.

        :param group_name: Name of the resource group.
        :type group_name: str
        :param service_name: Name of the service.
        :type service_name: str
        :param project_name: Name of the project.
        :type project_name: str
        :param task_name: Name of the Task.
        :type task_name: str
        :param parameters: Information about the task.
        :type parameters: ~azure.mgmt.datamigration.models.ProjectTask
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProjectTask, or the result of cls(response)
        :rtype: ~azure.mgmt.datamigration.models.ProjectTask
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ProjectTask"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-07-15-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'taskName': self._serialize.url("task_name", task_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'ProjectTask')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ProjectTask', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName}'}  # type: ignore

    def cancel(
        self,
        group_name,  # type: str
        service_name,  # type: str
        project_name,  # type: str
        task_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.ProjectTask"
        """Cancel a task.

        The tasks resource is a nested, proxy-only resource representing work performed by a DMS
        instance. This method cancels a task if it's currently queued or running.

        :param group_name: Name of the resource group.
        :type group_name: str
        :param service_name: Name of the service.
        :type service_name: str
        :param project_name: Name of the project.
        :type project_name: str
        :param task_name: Name of the Task.
        :type task_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ProjectTask, or the result of cls(response)
        :rtype: ~azure.mgmt.datamigration.models.ProjectTask
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ProjectTask"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-07-15-preview"
        accept = "application/json"

        # Construct URL
        url = self.cancel.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'taskName': self._serialize.url("task_name", task_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ProjectTask', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    cancel.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName}/cancel'}  # type: ignore

    def command(
        self,
        group_name,  # type: str
        service_name,  # type: str
        project_name,  # type: str
        task_name,  # type: str
        parameters,  # type: "_models.CommandProperties"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.CommandProperties"
        """Execute a command on a task.

        The tasks resource is a nested, proxy-only resource representing work performed by a DMS
        instance. This method executes a command on a running task.

        :param group_name: Name of the resource group.
        :type group_name: str
        :param service_name: Name of the service.
        :type service_name: str
        :param project_name: Name of the project.
        :type project_name: str
        :param task_name: Name of the Task.
        :type task_name: str
        :param parameters: Command to execute.
        :type parameters: ~azure.mgmt.datamigration.models.CommandProperties
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CommandProperties, or the result of cls(response)
        :rtype: ~azure.mgmt.datamigration.models.CommandProperties
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.CommandProperties"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-07-15-preview"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.command.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'groupName': self._serialize.url("group_name", group_name, 'str'),
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'projectName': self._serialize.url("project_name", project_name, 'str'),
            'taskName': self._serialize.url("task_name", task_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(parameters, 'CommandProperties')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ApiError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('CommandProperties', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    command.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.DataMigration/services/{serviceName}/projects/{projectName}/tasks/{taskName}/command'}  # type: ignore
