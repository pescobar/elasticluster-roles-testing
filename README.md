## Testing molecule with ElastiCluster roles

* Install elasticluster with [this script](https://gist.github.com/pescobar/3da5df9491a207cf0e06a22b28d1c9ee)

* Install all the python deps doing `pip install -r requirements.txt`

* Install Vagrant and VirtualBox

Now you are ready to do the first test:

```
$> cd ntpd/
$> molecule test
```

This should boot two vagrant VMs (centos7 and ubuntu16.04) and test the role:

* Check syntax with [yamlint](http://molecule.readthedocs.io/en/latest/configuration.html#yaml-lint)
* Check idempotence
* Check ansible best practices with [ansible-lint](https://github.com/willthames/ansible-lint)
* Run unit tests with [TestInfra](http://testinfra.readthedocs.io/en/latest/)
  * You can see the unit tests [here](ntpd/molecule/default/tests/test_default.py)
* Run the tests in Centos and Ubuntu
  * See the config [here](ntpd/molecule/default/molecule.yml)


## Future testing?

Try the [molecule openstack driver](http://molecule.readthedocs.io/en/latest/configuration.html#openstack)? 

Create a [cookiecutter template](https://github.com/metacloud/molecule/tree/master/molecule/cookiecutter) to automate
the creation of molecule configs for elasticluster?

Configure CI to run the tests automatically?


## drawbacks / issues

I could not use the `group_vars/all` provided by elasticluster. This is because
ElastiCluster recommends 1role >> 1repo but it can also be adapted to [Monolith Repo](http://molecule.readthedocs.io/en/latest/examples.html#monolith-repo)

