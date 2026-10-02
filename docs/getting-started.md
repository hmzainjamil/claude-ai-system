# Getting started

This repository is a personal Claude Code configuration snapshot, not a verified installer. Review the [root README](../README.md), [security notice](../SECURITY.md), and [historical system map](../SYSTEM_MAP.md) first.

## Inspect before adapting

Check your Claude Code version and current configuration using its official documentation. This repository does not declare a tested compatibility range. Inspect the exact skill, agent, or script you intend to use. Search for absolute paths, credential names, network requests, subprocesses, file deletion, browser control, and email or publishing actions.

The root has no `install.sh` or `.env.example`. Do not run bulk copy instructions from older documents. Back up your configuration and copy only reviewed files into the matching location in your own setup. Review hook configuration before enabling it; hooks can run automatically when their event fires.

## Credentials

Keep provider credentials in a local secret store or environment that is not tracked by Git. Do not paste keys into skills, workflow JSON, settings committed to a repository, or public issues. Check each script for the actual variable names and endpoints it uses; a name in an old guide does not guarantee current support.

## Verify your adaptation

Run only commands documented by the specific tool or script after reviewing its effects. Confirm paths and permissions for your operating system. This guide makes no claim that the repository scripts, integrations, schedules, or tests currently pass.

For source navigation, see the [documentation index](README.md), [skills reference](skills-reference.md), and [agents reference](agents-reference.md).
