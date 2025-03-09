"""Defines pydantic data models for resources that conforms to the AWX API.

These models ensure strong typing, data validation, and documentation for
attributes related to job execution.

Usage:
    >>> from models import JobTemplateModel
    >>> job_template = JobTemplateModel(
    ...     name="Deploy App",
    ...     inventory="inventory_1",
    ...     project="project_1",
    ...     playbook="deploy.yml"
    ... )

Warnings:

- Using high verbosity levels (`verbosity=5`) or large fork counts may lead
  to performance issues.
- If `ask_*` flags are enabled (e.g., `ask_variables_on_launch`), ensure
  the corresponding inputs are collected at runtime to avoid execution errors.
"""

from enum import Enum


class WebhookServiceEnum(str, Enum):
    """Defines the different webhook services.

    Type of webhook service:
        - `github` for GitHub integration.
        - `gitlab` for GitLab integration.

    Examples:
        >>> webhook_service = WebhookService.GITHUB
    """

    GITHUB = "github"
    GITLAB = "gitlab"


class JobTypeEnum(str, Enum):
    """Defines the different types of jobs.

    Type of job:
        - `run` for normal execution.
        - `check` for dry-run mode.
        - `scan` for analysis.

    Examples:
        >>> job_type = JobType.RUN
    """

    RUN = "run"
    CHECK = "check"
    SCAN = "scan"
