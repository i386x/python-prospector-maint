%if 0%{?fedora} || 0%{?rhel} > 7
# Add `--without python3' option (enable python3 by default):
%bcond_without python3
%if 0%{?fedora} > 26 || 0%{?rhel} > 7
%global defaultpython 3
%else
%global defaultpython 2
%endif
%else
# Add `--with python3' option (disable python3 by default):
%bcond_with python3
%global defaultpython 2
%endif

%global modname prospector

# Dependencies:
%global pylint_dep_lower < 2.0.0
%global pylint_dep_upper >= 1.5.6

Name:     python-%{modname}
Version:  0.12.11
Release:  1%{?dist}
Summary:  Prospector: python static analysis tool

Group:    Development/Tools

License:  GPLv2
URL:      http://prospector.readthedocs.io
Source0:  https://github.com/PyCQA/%{modname}/archive/%{version}.tar.gz
