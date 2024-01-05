Name: ruby
Version: 3.3.0
Release: 1%{?dist}
License: Ruby License/GPL - see COPYING
URL: http://www.ruby-lang.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
AutoReqProv: no
Requires: readline ncurses gdbm glibc openssl libyaml libffi zlib
BuildRequires: readline-devel ncurses-devel gdbm-devel glibc-devel gcc openssl-devel make libyaml-devel libffi-devel zlib-devel
Source0: https://cache.ruby-lang.org/pub/ruby/ruby-%{version}.tar.gz
Summary: An interpreter of object-oriented scripting language
Group: Development/Languages
Provides: ruby(abi) = 3.3
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel
Provides: rubygems
Obsoletes: ruby < %{version}
Obsoletes: ruby-devel < %{version}
Obsoletes: ruby-irb < %{version}
Obsoletes: ruby-libs < %{version}
Obsoletes: rubygem-bigdecimal
Obsoletes: rubygem-io-console
Obsoletes: rubygem-json
Obsoletes: rubygem-psych
Obsoletes: rubygem-rdoc
Obsoletes: rubygems

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing -std=gnu99"

%configure \
  --enable-shared \
  --disable-rpath \
  --without-X11 \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir}

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

#we don't want to keep the src directory
rm -rf $RPM_BUILD_ROOT/usr/src

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}/*
%{_includedir}/*
%{_datadir}/*
%{_libdir}/*

%changelog

* Fri Jan 05 2024 Vitaliy Serov <vitaliy.serov@onlyoffice.com> - 3.3.0
- Add new spec for ruby 3.3.0

* Thu Mar 30 2023 feedforce tech team <technical_staff@feedforce.jp> - 3.2.2
- Update ruby version to 3.2.2

* Wed Feb 08 2023 feedforce tech team <technical_staff@feedforce.jp> - 3.2.1
- Update ruby version to 3.2.1

* Wed Jan 04 2023 John Balyozian <jbalyozian@onedoor.com> - 3.2.0
- Update ruby version to 3.2.0

* Tue Apr 12 2022 feedforce tech team <technical_staff@feedforce.jp> - 3.0.4
- Update ruby version to 3.0.4

* Wed Nov 24 2021 feedforce tech team <technical_staff@feedforce.jp> - 3.0.3
- Update ruby version to 3.0.3

* Wed Jul 07 2021 feedforce tech team <technical_staff@feedforce.jp> - 3.0.2
- Update ruby version to 3.0.2

* Wed Apr 07 2021 feedforce tech team <technical_staff@feedforce.jp> - 3.0.1
- Update ruby version to 3.0.1

* Wed Apr 07 2021 Tsubasa Takayama <t-takayama@feedforce.jp> - 3.0.0
- Update ruby version to 3.0.0

* Mon Apr 05 2021 feedforce tech team <technical_staff@feedforce.jp> - 2.7.3
- Update ruby version to 2.7.3

* Fri Oct 02 2020 feedforce tech team <technical_staff@feedforce.jp> - 2.7.2
- Update ruby version to 2.7.2

* Wed Apr 01 2020 feedforce tech team <technical_staff@feedforce.jp> - 2.7.1
- Update ruby version to 2.7.1

* Thu Jan 02 2020 Mike MacDonald <crazymykl@gmail.com> - 2.7.0
- Update ruby version to 2.7.0

* Tue Oct 01 2019 feedforce tech team <technical_staff@feedforce.jp> - 2.6.5
- Update ruby version to 2.6.5

* Wed Aug 28 2019 feedforce tech team <technical_staff@feedforce.jp> - 2.6.4
- Update ruby version to 2.6.4

* Wed Apr 17 2019 feedforce tech team <technical_staff@feedforce.jp> - 2.6.3
- Update ruby version to 2.6.3

* Wed Mar 13 2019 feedforce tech team <technical_staff@feedforce.jp> - 2.6.2
- Update ruby version to 2.6.2

* Wed Jan 30 2019 feedforce tech team <technical_staff@feedforce.jp> - 2.6.1
- Update ruby version to 2.6.1

* Tue Dec 25 2018 feedforce tech team <technical_staff@feedforce.jp> - 2.6.0
- Update ruby version to 2.6.0

* Fri Oct 19 2018 Masataka Suzuki <koshigoe@feedforce.jp> - 2.5.3
- Update ruby version to 2.5.3

* Thu Oct 18 2018 Masataka Suzuki <koshigoe@feedforce.jp> - 2.5.2
- Update ruby version to 2.5.2

* Thu Mar 29 2018 Masataka Suzuki <koshigoe@feedforce.jp> - 2.5.1
- Update ruby version to 2.5.1

* Mon Dec 25 2017 Takashi Masuda <masutaka@feedforce.jp> - 2.5.0
- Update ruby version to 2.5.0

* Fri Dec 15 2017 Masataka Suzuki <koshigoe@feedforce.jp> - 2.4.3
- Update ruby version to 2.4.3

* Fri Sep 15 2017 Masataka Suzuki <koshigoe@feedforce.jp> - 2.4.2
- Update ruby version to 2.4.2

* Thu Mar 23 2017 Masataka Suzuki <koshigoe@feedforce.jp> - 2.4.1
- Update ruby version to 2.4.1

* Mon Dec 26 2016 Takashi Masuda <masutaka@feedforce.jp> - 2.4.0
- Update ruby version to 2.4.0

* Tue Nov 22 2016 Masato Tanaka <tanaka@feedforce.jp> - 2.3.3
- Update ruby version to 2.3.3

* Wed Nov 16 2016 Masato Tanaka <tanaka@feedforce.jp> - 2.3.2
- Update ruby version to 2.3.2

* Tue Apr 26 2016 Takashi Masuda <masutaka@feedforce.jp> - 2.3.1
- Update ruby version to 2.3.1

* Tue Dec 25 2015 Masato Tanaka <tanaka@feedforce.jp> - 2.3.0
- Update ruby version to 2.3.0

* Tue Dec 17 2015 Masato Tanaka <tanaka@feedforce.jp> - 2.2.4
- Update ruby version to 2.2.4

* Tue Aug 19 2015 Masato Tanaka <tanaka@feedforce.jp> - 2.2.3
- Update ruby version to 2.2.3

* Tue Apr 14 2015 Takashi Masuda <masutaka@feedforce.jp> - 2.2.2
- Update ruby version to 2.2.2

* Wed Mar  4 2015 Shota Miyamoto <miyamoto@feedforce.jp> - 2.2.1
- Update ruby version to 2.2.1

* Fri Dec 26 2014 Kenta ONISHI <onishi@feedforce.jp> - 2.2.0
- Version bumped to 2.2.0

* Fri Nov 14 2014 Takashi Masuda <masutaka@feedforce.jp> - 2.1.5
- Update ruby version to 2.1.5
- Remove dependency unzip

* Wed Nov  5 2014 Takashi Masuda <masutaka@feedforce.jp> - 2.1.4-2
- Remove dependency db4 and db4-devel

* Fri Oct 31 2014 Takashi Masuda <masutaka@feedforce.jp> - 2.1.4
- Update ruby version to 2.1.4

* Wed Oct 29 2014 Takashi Masuda <masutaka@feedforce.jp> - 2.1.2
- Remove dependencies on tcl-devel and byacc

* Fri May  9 2014 Masahito Yoshida <masahito@axsh.net> - 2.1.2
- Update ruby version to 2.1.2

* Thu Dec 26 2013 Masahito Yoshida <masahito@axsh.net> - 2.1.0
- Update ruby version to 2.1.0

* Sat Nov 23 2013 Masahito Yoshida <masahito@axsh.net> - 2.0.0-p353
- Update ruby version to 2.0.0-p353

* Tue Jul  2 2013 Masahito Yoshida <masahito@axsh.net> - 2.0.0-p247
- Update ruby version to 2.0.0-p247

* Sun May 19 2013 Masahito Yoshida <masahito@axsh.net> - 2.0.0-p195
- Update ruby version to 2.0.0-p195

* Sat Mar 23 2013 Masahito Yoshida <masahito@axsh.net> - 2.0.0-p0
- Update ruby version to 2.0.0-p0

* Sun Feb 24 2013 Masahito Yoshida <masahito@axsh.net> - 1.9.3-p392
- Update ruby version to 1.9.3-p392

* Tue Jan 29 2013 Carlos Villela <cv@lixo.org> - 1.9.3-p374
- Update ruby version to 1.9.3-p374

* Tue Jan 15 2013 Carlos Villela <cv@lixo.org> - 1.9.3-p362
- Update ruby version to 1.9.3-p362

* Thu Nov 15 2012 Rajat Vig <rajat.vig@gmail.com> - 1.9.3-p327
- Update ruby version to 1.9.3-p327

* Mon Oct 22 2012 Carlos Villela <cv@lixo.org> - 1.9.3-p286
- Update ruby version to 1.9.3-p286

* Wed Jul 4 2012 Carlos Villela <cv@lixo.org> - 1.9.3-p194
- Update ruby version to 1.9.3-p194

* Wed Jan 18 2012 Mandi Walls <mandi.walls@gmail.com> - 1.9.3-p0
- Update ruby version to 1.9.3-p0

* Mon Aug 29 2011 Gregory Graf <graf.gregory@gmail.com> - 1.9.2-p290
- Update ruby version to 1.9.2-p290

* Sat Jun 25 2011 Ian Meyer <ianmmeyer@gmail.com> - 1.9.2-p180-2
- Remove non-existant --sitearchdir and --vedorarchdir from %configure
- Replace --sitedir --vendordir with simpler --libdir
- Change %{_prefix}/share to %{_datadir}

* Mon Mar 7 2011 Robert Duncan <robert@robduncan.co.uk> - 1.9.2-p180-1
- Update prerequisites to include make
- Update ruby version to 1.9.2-p180
- Install /usr/share documentation
- (Hopefully!?) platform agnostic

* Sun Jan 2 2011 Ian Meyer <ianmmeyer@gmail.com> - 1.9.2-p136-1
- Initial spec to replace system ruby with 1.9.2-p136
