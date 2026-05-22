"""Diagnostics: health checks and environment probing."""

from ctxsift.diagnostics.doctor import (
    DoctorCheck,
    DoctorReport,
    collect_doctor_report,
    collect_doctor_report_for_config,
    render_doctor_report,
    render_doctor_report_rich,
)

__all__ = [
    "DoctorCheck",
    "DoctorReport",
    "collect_doctor_report",
    "collect_doctor_report_for_config",
    "render_doctor_report",
    "render_doctor_report_rich",
]
