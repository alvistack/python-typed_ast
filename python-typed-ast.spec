# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-typed-ast
Epoch: 100
Version: 1.5.4
Release: 1%{?dist}
Summary: Modified fork of CPython's ast module
License: Apache-2.0
URL: https://github.com/python/typed_ast/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
typed_ast is a Python 3 package that provides a Python 2.7 and Python 3
parser similar to the standard ast library. Unlike ast up to Python 3.7,
the parsers in typed_ast include PEP 484 type comments and are
independent of the version of Python under which they are run. The
typed_ast parsers produce the standard Python AST (plus type comments),
and are both fast and correct, as they are based on the CPython 2.7 and
3.7 parsers. typed_ast runs on CPython 3.6-3.10 on Linux, OS X and
Windows.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-typed-ast
Summary: Modified fork of CPython's ast module
Requires: python3
Provides: python3-typed_ast = %{epoch}:%{version}-%{release}
Provides: python3-typed-ast = %{epoch}:%{version}-%{release}
Provides: python3dist(typed-ast) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-typed-ast = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(typed-ast) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-typed-ast = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(typed-ast) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-typed-ast
typed_ast is a Python 3 package that provides a Python 2.7 and Python 3
parser similar to the standard ast library. Unlike ast up to Python 3.7,
the parsers in typed_ast include PEP 484 type comments and are
independent of the version of Python under which they are run. The
typed_ast parsers produce the standard Python AST (plus type comments),
and are both fast and correct, as they are based on the CPython 2.7 and
3.7 parsers. typed_ast runs on CPython 3.6-3.10 on Linux, OS X and
Windows.

%files -n python%{python3_version_nodots}-typed-ast
%license LICENSE
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-typed-ast
Summary: Modified fork of CPython's ast module
Requires: python3
Provides: python3-typed_ast = %{epoch}:%{version}-%{release}
Provides: python3-typed-ast = %{epoch}:%{version}-%{release}
Provides: python3dist(typed-ast) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-typed-ast = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(typed-ast) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-typed-ast = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(typed-ast) = %{epoch}:%{version}-%{release}

%description -n python3-typed-ast
typed_ast is a Python 3 package that provides a Python 2.7 and Python 3
parser similar to the standard ast library. Unlike ast up to Python 3.7,
the parsers in typed_ast include PEP 484 type comments and are
independent of the version of Python under which they are run. The
typed_ast parsers produce the standard Python AST (plus type comments),
and are both fast and correct, as they are based on the CPython 2.7 and
3.7 parsers. typed_ast runs on CPython 3.6-3.10 on Linux, OS X and
Windows.

%files -n python3-typed-ast
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-typed-ast
Summary: Modified fork of CPython's ast module
Requires: python3
Provides: python3-typed_ast = %{epoch}:%{version}-%{release}
Provides: python3-typed-ast = %{epoch}:%{version}-%{release}
Provides: python3dist(typed-ast) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-typed-ast = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(typed-ast) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-typed-ast = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(typed-ast) = %{epoch}:%{version}-%{release}

%description -n python3-typed-ast
typed_ast is a Python 3 package that provides a Python 2.7 and Python 3
parser similar to the standard ast library. Unlike ast up to Python 3.7,
the parsers in typed_ast include PEP 484 type comments and are
independent of the version of Python under which they are run. The
typed_ast parsers produce the standard Python AST (plus type comments),
and are both fast and correct, as they are based on the CPython 2.7 and
3.7 parsers. typed_ast runs on CPython 3.6-3.10 on Linux, OS X and
Windows.

%files -n python3-typed-ast
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog
