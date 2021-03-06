## v2.3.0

Catch undefined __salt__ error
Add missing require to upstart container config
Improve run_container scripts output
Remove extraneous onchanges condition
Add require for systemd service on the service file
Add support for systemd
Update documentation to reflect ulimits support in in pillars.
Enable ulimit opts on docker startup
Support for ulimits in docker
Fix weird tabs
Fixing readme links
Merge pull request #70 from ministryofjustice/minor-get-region-fix
Import boto as needed by get_region function.
Merge pull request #69 from ministryofjustice/bump-formula-requirements
Bump formula requirements.
Merge pull request #68 from ministryofjustice/hope-never-dies
Sleep after start to fix race condition between docker/upstart
Fix indentation and style.
Docker inspect commands need || true to unbreak upstart jobs.
Fix database endpoint environment variables documentation
Backport fix preventing exception during dockerng.list_tags
Fix elb_reg region argument defaults
Enable multiregion support
Bump docker-formulas as new docker version is now required.
Salt 2014.7.x compatibility
Backport dockerng states from newer salt.


## v2.1.6
* Fix branchrunner docker env creation
* Update branchrunner docs on dns lookup
* Fix branchrunner container ports

## v2.1.5

* Fix branchrunner upstart script

## v2.1.4

* Update python-formula to 1.1.5

## v2.1.3

* Update python-formula to 1.1.4

## v2.1.2

* Update ntp and python formulas

## v2.1.1

* Update formulas

## v2.1.0
* Make unattended upgrades the default setting

## v2.0.0
* Add alias option to links
* Use docker introspect running state for checking containers
* Fix broken error handling on containers missing on introspect
* Increase retry count to 10
* Trigger on any parent service started event
* Add alias to docker link command
* Change container linking pillar structure

## v1.4.3

Added support for container linking

## v1.4.2

Added support for setting arbitrary nginx Headers and Values directly from the Pillar.

## v1.4.1
Features:

Add support for basic http auth in nginx proxy on a per container basis.


## v1.4.0

Features:
* Allow overriding database settings in the pillar
* Allow disabling the default server setting on a vhost
Fixes:
* Add documentation for setting up branchrunner

## v1.3.6

Features:
* Updated nginx-formula dependency to v3.3.4

Fixes:
* custom nginx json log formats resulting in unparseable double-quoted json

## v1.3.5
Fixes:
* docker pulling the wrong tag 

## v1.3.4

* Add elasticache docker envs if available
* Enable clustering of containers with containers in other EC2 instances
Features:
* Update nginx-formula version to 3.3.3

## v1.3.3

Fixes:
  * Revert Remove require on requests

Features:
* Update nginx version to 3.3.2

## v1.3.1

Fixes:
* Remove require on requests

## v1.3.0

* Add an initial_version option to the container pillar
* Update nginx version to 3.3.1

## v1.2.0

Features:
* updated nginx-formula to 3.3.0, for the new log file/format customisation
* allowed customization of nginx log format
* Add ability to cluster containers with other hosts containers

Fixes:
* Strip dots from branch name subdomain host name
* Updated README
* Add a fallback check to the pillar for a containers host port
>>>>>>> master
* Fix macro calls introduced for nginx logs

## v1.0.6

* Fix macro import for cleanup containers

## v1.0.5

* Set a default nginx host to avoid branch confusion

## v1.0.4

* Bump aws-formula version to 0.4.3

## v1.0.3

* use grains from aws formula for elb name

## v1.0.2

* Move _states to root directory

## v1.0.0

* Initial release as split out from ministryofjustice/template-deploy
