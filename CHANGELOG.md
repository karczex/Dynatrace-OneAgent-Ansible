## **1.2.71**&emsp;<sub><sup>2025-05-15 (24a8364b4ca09000644326cb99f2a016c9a54440...0c3b17ec8870437e38d5e179fbe308edb46faf86)</sup></sub>

### Features

- fake commit (c91a1fa78366db1d04880618e69a4060ef9b8f53)

<br>

## **1.2.66**&emsp;<sub><sup>2025-05-14 (20e499de8a4c0dff4c3eee2c3c8093132b5a1e4b...d8e1984b55e33af17e206b478c8b59e29b374cf3)</sup></sub>

### Features

- fake commit \+1 (d8e1984b55e33af17e206b478c8b59e29b374cf3)

<br>

## **1.2.63**&emsp;<sub><sup>2025-05-14 (36eae88e568b537ed190381df37d3b554d52761c...36eae88e568b537ed190381df37d3b554d52761c)</sup></sub>

*no relevant changes*
<br>

## **1.2.61**&emsp;<sub><sup>2025-05-14 (4bb2c74eadc0050c337ff59c2edf9898c2de8d05...4bb2c74eadc0050c337ff59c2edf9898c2de8d05)</sup></sub>

*no relevant changes*
<br>

## [1.2.4] - 2025-04-30
- Added parameter `oneagent_no_log` controlling Ansible no_log attribute

## [1.2.3] - 2025-02-03
- Fixed issue with skipping CA certificate transfer task

## [1.2.2] - 2025-10-1
- Fixed linters issues

## [1.2.1] - 2024-12-19
- Fixed problem with installer signature verification on AIX
- Added LICENSE file

## [1.2.0] - 2024-11-29

- Added parameter `--restart-service` parameter, once OneAgent configuration is performed
- Fixed problem with `Invalid version string` during collection install
- Added parameter `oneagent_verify_signature` controlling signature verification step
- Removed `oneagent_validate_certs` parameter
- Fixed problem with `dt-root.cert.pem` not being copied to the target host
- Added ability for downloading installer's certificate if the certificate is not embedded in the collection

## [1.1.0] - 2021-10-06

- Fixed malformation of `--restart-service` parameter, passed to `oneagentctl`.
- Fixed problem with installation for higher versions of Ansible.
- Improved `oneagentctl` configuration mechanism.

## [1.0.0] - 2021-08-13

- Added capability of creating download directory structure during deployment.
- Added `oneagent_validate_certs` parameter.
- Added capability of cleaning up downloaded artifacts in case of deployment's failure.

## [0.4.0] - 2021-06-25

- Removed `oneagent_remove_signature` parameter.
- Added ability to configure installation using `oneagentctl`.
- Removed the need to provide the required parameters in case of uninstallation.
- Added node restart option.

## [0.3.0] - 2021-02-12

- Fixed role's idempotence.

## [0.2.1] - 2020-12-28

- Fixed minor problems with example playbooks and inventory files.

## [0.2.0] - 2020-11-18

- Added new parameter `oneagent_platform_install_args` allowing to specify platform-specific installer arguments.
- Changed `oneagent_local_installer` parameter to pass only single path to local installer.

## [0.1.0] - 2020-09-25

- Initial [Preview](https://www.dynatrace.com/support/help/shortlink/preview-and-early-adopter-releases) release.
