# Pod Chaos Monkey

Pod chaos monkey is a PoC of chaos engineering for Kubernetes which will help us to test the reliability of our system. It will kill pods (once at a time), in a desired namespace, in a schedule.

This PoC has been developed using [Python](https://www.python.org/) 3.10

The project contains a [Makefile](./Makefile) to make easier the interaction with it.

## Local Python Environment

Create a local environment to develop/test your python code.

```bash
$ make local-environment
```


## Unit test

Run unit tests

```bash
$ make unittest
```

## Create local Kubernetes cluster (KinD)

[Docker](https://www.docker.com/) is mandatory because is a hard requirement of [Kind](https://kind.sigs.k8s.io/).

```bash
$ make kind
```

Once that you have your Kubernetes cluster, you can create some pods:

```bash
$ kubectl run nginx1 --image=nginx
```

## Environment Variables

* **ENVIRONMENT**: Environment where the software will be running (*KUBERNETES*, *LOCAL*). By default: *KUBERNETES*.
* **LOGGER_LEVEL**: Level for the logger. By default: *INFO*


## Build Docker image

```bash
$ TAG=<desired tag> make docker-build
```

## Load Image into Kubernetes

Your desired image will be loaded into the kubernetes node.

```bash
$ TAG=<desired tag> make load-image
```

## Install Helm Chart

It will install the [helm chart](./chart/) with the default [values](./chart/values.yaml).

```bash
$ make helm-install
```

Helm chart values file contains the docker image, cron value and namespace where the pods will be removed.
You can apply your own values.

**example:**

```yaml
image: pod-chaos-monkey:latest
schedule: "* * * * *"
namespace: default
```

## Destroy your cluster

```bash
$ make destroy
```
