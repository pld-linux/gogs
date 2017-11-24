Summary:	Self-hosted Git service
Name:		gogs
Version:	0.11.34
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	https://github.com/gogits/gogs/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ee0ad6f4eb808fb4113ddd429ddc3ddd
URL:		https://gogs.io/
BuildRequires:	golang >= 1.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages 0
%define		gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};
%define		gopath		%{_libdir}/golang
%define		import_path	github.com/gogits/%{name}

%description
Self-hosted Git service.

%prep
%setup -qc

mv %{name}-%{version}/{README*,LICENSE} .
install -d src/$(dirname %{import_path})
mv %{name}-%{version} src/%{import_path}

%build
export GOPATH=$(pwd)

%gobuild -o bin/%{name} %{import_path}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p bin/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%doc %lang(zh) README_ZH.md
%attr(755,root,root) %{_bindir}/gogs
