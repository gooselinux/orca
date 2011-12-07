%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%global debug_package %{nil}

%define python_version 2.5
%define pyorbit_version 2.0.1
%define pygtk2_version 2.6.2
%define gnome_python_version 2.6.2
%define gnome_python_version 2.6.2
%define brltty_version 3.7.2
%define atk_version 1.11.3
%define gail_version 1.8.11
%define gnome_speech_version 0.3.10
%define libspi_version 1.7.6
%define brlapi_version 0.4.1
%define brltty_version 3.7.2
%define control_center_version 2.16.0-5

Name:		orca
Version:	2.28.2
Release: 	1%{?dist}
Summary:	Assistive technology for people with visual impairments

Group:		User Interface/Desktops
License:	LGPLv2+
URL:		http://projects.gnome.org/orca/
Source0:	http://download.gnome.org/sources/orca/2.28/orca-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	python-devel >= %{python_version}
BuildRequires:	brlapi-devel >= %{brlapi_version}
BuildRequires:	brltty >= %{brltty_version}
BuildRequires:	pyorbit-devel >= %{pyorbit_version}
BuildRequires: 	pygtk2-devel >= %{pygtk2_version}
BuildRequires:	atk-devel >= %{atk_version}
BuildRequires:	gail-devel >= %{gail_version}
BuildRequires:	at-spi-devel >= %{libspi_version}
BuildRequires:	gnome-speech-devel >= %{gnome_speech_version}
BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:  gnome-python2-bonobo
BuildRequires:  gnome-python2-libwnck
BuildRequires:  gnome-python2-gconf
BuildRequires:  at-spi-python
BuildRequires:  dbus-python
Obsoletes:	gnopernicus
Provides:	gnopernicus

Requires:	gnome-mag
Requires:	control-center >= %{control_center_version}
Requires:	at-spi-python
Requires:	gnome-python2-bonobo
Requires:	gnome-python2-libwnck
Requires:       gnome-python2-gconf
Requires:	gnome-python2-gnome
Requires:	gnome-speech

%description
Orca is a flexible, extensible, and powerful assistive technology for people
with visual impairments. Using various combinations of speech synthesis,
braille, and magnification, Orca helps provide access to applications and
toolkits that support AT-SPI (e.g. the GNOME desktop).

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

find $RPM_BUILD_ROOT -name '*.la' | xargs rm -f

#remove the .desktop file since we configure orca through the accessibility capplet
find $RPM_BUILD_ROOT -name '*.desktop' | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
update-desktop-database &> /dev/null ||:
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README
%{_bindir}/orca
%{python_sitearch}/orca
%{_datadir}/icons/hicolor/*/apps/orca.png
%{_datadir}/icons/hicolor/scalable/apps/orca.svg
%{_datadir}/orca
%{_mandir}/man1/orca.1.gz


%changelog
* Mon Jan  4 2010 Matthias Clasen <mclasen@redhat.com> - 2.28.2-1
- Update to 2.28.2, sync with Fedora 12

* Mon Oct 19 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.1-1
- Update to 2.28.1

* Tue Sep 22 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Mon Sep  7 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.92-1
- Update to 2.27.92

* Mon Aug 24 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.91-1
- Update to 2.27.91

* Mon Aug 10 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.90-1
- Update to 2.27.90

* Tue Jul 28 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.5-1
- Update to 2.27.5

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.4-1
- Update to 2.27.4

* Thu Jun 18 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.3-2
- We don't have debuginfo

* Tue Jun 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.3-1
- Update to 2.27.3

* Thu Jun 11 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.2-2
- Add a dependency on gnome-speech (#503193)

* Sun May 31 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.2-1
- Update to 2.27.2

* Mon Apr 13 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.1-1
- Update to 2.26.1
- See http://download.gnome.org/sources/orca/2.26/orca-2.26.1.news

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Mon Mar  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.92-1
- Update to 2.25.92

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.91-1
- Update to 2.25.91

* Tue Feb  3 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.90-1
- Update to 2.25.90

* Tue Jan 20 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.5-1
- Update to 2.25.5

* Tue Jan  6 2009 Matthias Clasen <mclasen@redhat.com> - 2.25.4-1
- Update to 2.25.4

* Wed Dec 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.3-2
- Update to 2.25.3

* Wed Dec  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.2-2
- Rebuild for Python 2.6

* Wed Dec  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.2-1
- Update to 2.25.2

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.25.1-3
- Rebuild for Python 2.6

* Fri Nov 21 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.1-2
- Tweak description

* Wed Nov 12 2008 Matthias Clasen <mclasen@redhat.com> - 2.25.1-1
- Update to 2.25.1

* Fri Oct 17 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Mon Sep  8 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.92-1
- Update to 2.23.92

* Tue Sep  2 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Tue Aug 26 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.90-2
- Require gnome-python2-gnome

* Sat Aug 23 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.90-1
- Update to 2.23.90

* Tue Aug  5 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.6-1
- Update to 2.23.6

* Tue Jul 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.5-1
- Update to 2.23.5

* Wed Jun 18 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.4-1
- Update to 2.23.4

* Tue Jun  3 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.3-1
- Update to  2.23.3

* Wed May 28 2008 Jon McCann <jmccann@redhat.com> - 2.23.2-3
- Add BuildRequires gnome-python2-bonobo back

* Wed May 28 2008 Jon McCann <jmccann@redhat.com> - 2.23.2-2
- Require gnome-python2-bonobo and gnome-python2-libwnck

* Tue May 13 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.2-1
- Update to 2.23.2

* Sun May  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-2
- Fix source url

* Fri Apr 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-1
- Update to 2.23.1

* Mon Apr  7 2008 Jon McCann <jmccann@redhat.com> - 2.22.1-2
- Fix signal handling (GNOME bug #525831)

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.1-1
- Update to 2.22.1

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Mon Feb 25 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.92-1
- Update to 2.21.92

* Tue Feb 12 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.91-1
- Update to 2.21.91

* Tue Jan 29 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.90-1
- Update to 2.21.90

* Mon Jan 14 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.5-1
- Update to 2.21.5

* Fri Jan  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.21.4-2
- Require at-spi-python (#427432)

* Tue Dec 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.4-1
- Update to 2.21.4

* Wed Dec  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.3-1
- Update to 2.21.3

* Tue Nov 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.2-1
- Update to 2.21.2

* Mon Oct 15 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0.1-1
- Update to 2.20.0.1 (bug fixes and translation updates)

* Sun Sep 16 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Tue Sep  4 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.92-1
- Update to 2.19.92

* Mon Aug 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.90-1
- Update to 2.19.90

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-2
- Update license field

* Sun Jul 29 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.6-1
- Update to 2.19.6

* Mon Jul  9 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.5-1
- Update to 2.19.5

* Sun Jun 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.4-1
- Update to 2.19.4

* Tue Jun  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.3-1
- Update to 2.19.3

* Sun May 20 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.2-1
- Update to 2.19.2

* Tue Mar 13 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Wed Feb 28 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.92-1
- Update to 2.17.92

* Sun Feb 11 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.91-1
- Update to 2.17.91

* Mon Jan 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.90-1
- Update to 2.17.90

* Thu Jan 11 2007 Matthias Clasen <mclasen@redhat.com> - 2.17.5-1
- Update to orca 2.17.5

* Wed Dec 19 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.4-1
- Update to orca 2.17.4

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 2.17.3-2
- rebuild for python 2.5

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.3-1
- Update to orca 2.17.3

* Tue Nov  7 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.2-1
- Update to orca 2.17.2

* Tue Nov  7 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.1-2
- Fix typos in the spec

* Sat Oct 21 2006 Matthias Clasen <mclasen@redhat.com> - 2.17.1-1
- Update to 2.17.1

*  Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 1.0.0-4
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 John (J5) Palmieri <johnp@redhat.com> - 1.0.0-3
- Add patch to shutdown orca

* Tue Sep 19 2006 John (J5) Palmieri <johnp@redhat.com> - 1.0.0-2
- Add requirements on gnome-mag and newer version of control-center
- remove .desktop file and make control-center start and configure orca

* Sun Sep  3 2006 Matthias Clasen <mclasen@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Thu Aug 31 2006 Matthias Clasen <mclasen@redhat.com> - 0.9.0-4
- Obsolete gnome-mag-devel, too

* Tue Aug 29 2006 John (J5) Palmieri <johnp@redhat.com> - 0.9.0-3
- Spec file cleanups

* Mon Aug 21 2006 John (J5) Palmieri <johnp@redhat.com> - 0.9.0-1
- Initial package
