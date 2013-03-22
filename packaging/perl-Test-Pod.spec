#
# spec file for package perl-Test-Pod
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#



Name:           perl-Test-Pod
Version:        1.45
Release:        1
License:        Artistic-2.0 or GPL-2.0
%define cpan_name Test-Pod
Summary:        check for POD errors in files
Url:            http://search.cpan.org/dist/Test-Pod/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/D/DW/DWHEELER/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Simple) >= 3.05
BuildRequires:  perl(Test::More) >= 0.62
Requires:       perl(File::Spec)
Requires:       perl(Pod::Simple) >= 3.05
Requires:       perl(Test::Builder::Tester) >= 1.02
Requires:       perl(Test::More) >= 0.62
BuildArch:      noarch

%description
Check POD files for errors or warnings in a test file, using 'Pod::Simple'
to do the heavy lifting.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(644,root,root,755)

%changelog
