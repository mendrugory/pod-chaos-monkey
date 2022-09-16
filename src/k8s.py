import random
from kubernetes import client, config
from config import get_logger, get_environment, ENV_KUBERNETES


logger = get_logger()

def get_core_client():
    '''
    get_client returns a kubernetes client (core)
    :return: object | None
    '''
    try:
        __load_kubernetes_config()
    except config.config_exception.ConfigException as e:
        logger.error(e)
        return None

    return client.CoreV1Api()

def remove_random_pod(client, namespace):
    """
    remove_random_pod removes a random pod from the given namespace
    :param client: kubernetes api client
    :param namespace:
    :return: None
    """
    pods = __get_pods(client, namespace)
    if pods:
        pod = random.choice(pods)
        return __remove_pod(client, pod)
        
    return None

def __load_kubernetes_config():
    '''
    __load_kubernetes_config loads kubernetes configuration depending on the environment
    '''
    environment = get_environment()
    if environment==ENV_KUBERNETES:
        config.load_incluster_config()
    else:
        config.load_kube_config()

def __get_pods(client, namespace):
    """
    Get pods from the given namespace
    :param client: kubernetes client
    :param namespace: a kubernetes namespace name
    :return: list of pods
    """
    pod_list = client.list_namespaced_pod(namespace)
    return pod_list.items

def __remove_pod(client, pod):
    """
    __remove_pod removes a pod
    :param client: kubernetes api client
    :return: None
    """
    return client.delete_namespaced_pod(
        name=pod.metadata.name,
        namespace=pod.metadata.namespace
    )
