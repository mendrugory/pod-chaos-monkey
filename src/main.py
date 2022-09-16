import click
from config import get_logger
from k8s import get_core_client, remove_random_pod

logger = get_logger()

@click.group()
def root():
    '''
    Simple CLI
    '''
    logger.info("Monkeys are going to mess up your pods")


@root.command(name='mess_up', help='mess_up will remove a pod (random) within the given namespace')
@click.argument('namespace')
def mess_up(namespace):
    '''
    mess_up removes a random pod from the given namespace
    :param namespace: namespace where the pod will be removed
    '''
    try:
        client = get_core_client()
        if client is None:
            logger.error("no kubernetes client. Check if you have permission to connect to the cluster.")
            return

        removed_pod = remove_random_pod(client, namespace)
        if removed_pod is None:
            logger.info(f"no pods in {namespace}")
            return

        logger.info(f"pod {removed_pod.metadata.namespace}/{removed_pod.metadata.name} was removed.")

    except Exception as e:
        logger.error(f"error: {e}")


if __name__ == '__main__':
    root()
