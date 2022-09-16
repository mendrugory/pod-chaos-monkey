import unittest
from kubernetes.client.models import V1PodList, V1Pod, V1ObjectMeta
from k8s import remove_random_pod


class K8sTest(unittest.TestCase):
    def test_remove_random_pod(self):
        namespace = "default"
        n_pods = 10
        client = MockK8sClient(namespace, n_pods)
        pod = remove_random_pod(client, namespace)
        self.assertIsNotNone(pod)
        self.assertEqual(len(client.pods[namespace]), n_pods - 1)

    def test_remove_random_pod_empty_namespace(self):
        namespace = "default"
        n_pods = 0
        client = MockK8sClient(namespace, n_pods)
        pod = remove_random_pod(client, namespace)
        self.assertIsNone(pod)


class MockK8sClient:
    def __init__(self, namespace, n_pods):
        self.pods = {namespace: dict()}
        for i in range(0, n_pods):
            name = f"pod-{i}"
            self.pods[namespace][name] = V1Pod(api_version="v1", kind="Pod", metadata = V1ObjectMeta(name=name, namespace=namespace))

            
    def delete_namespaced_pod(self, name=None, namespace=None):
        if namespace in self.pods and name in self.pods[namespace]:
            pod = self.pods[namespace][name]
            del self.pods[namespace][name]
            return pod

    def list_namespaced_pod(self, namespace):
        values = []
        if namespace in self.pods:
            values = list(self.pods[namespace].values())

        pod_list = V1PodList(api_version="v1", kind="PodList", items=values)
        return pod_list


if __name__ == '__main__':
    unittest.main()
