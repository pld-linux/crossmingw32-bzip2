%define		realname		bzip2
Summary:	Extremely powerful file compression utility - MinGW32 cross version
Summary(es.UTF-8):	Un compresor de archivos con un nuevo algoritmo
Summary(fr.UTF-8):	Utilitaire de compression de fichier extrêmement puissant
Summary(pl.UTF-8):	Kompresor plików bzip2 - wersja skrośna dla MinGW32
Summary(pt_BR.UTF-8):	Compactador de arquivo extremamente poderoso
Summary(uk.UTF-8):	Компресор файлів на базі алгоритму блочного сортування
Summary(ru.UTF-8):	Компрессор файлов на основе алгоритма блочной сортировки
Name:		crossmingw32-%{realname}
Version:	1.0.7
Release:	1
License:	BSD-like
Group:		Applications/Archiving
Source0:	https://sourceware.org/pub/bzip2/%{realname}-%{version}.tar.gz
# Source0-md5:	1a6a61cc867be4f3d6549037a09bf13e
Patch0:		%{name}.patch
URL:		https://sourceware.org/bzip2/
BuildRequires:	crossmingw32-gcc
Requires:	crossmingw32-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32

%define		_sysprefix		/usr
%define		_prefix			%{_sysprefix}/%{target}
%define		_libdir			%{_prefix}/lib
%define		_dlldir			/usr/share/wine/windows/system
%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%ifnarch %{ix86}
# arch-specific flags (like alpha's -mieee) are not valid for i386 gcc
%define		optflags	-O2
%endif
# -z options are invalid for mingw linker, most of -f options are Linux-specific
%define		filterout_ld	-Wl,-z,.*
%define		filterout_c	-f[-a-z0-9=]*

%description
Bzip2 compresses files using the Burrows-Wheeler block-sorting text
compression algorithm, and Huffman coding. Compression is generally
considerably better than that achieved by more conventional
LZ77/LZ78-based compressors, and approaches the performance of the PPM
family of statistical compressors. The command-line options are
deliberately very similar to those of GNU Gzip, but they are not
identical.

%description -l es.UTF-8
Bzip2 es un programa de compresión/descompresión. Típicamente el
archivo compactado queda entre 20 la 30 por ciento menor de que se
fuera compactado con gzip. Observa que bzip2 no entiende los archivos
del bzip original, ni los archivos del gzip.

%description -l fr.UTF-8
Bzip2 compresse des fichiers en utilisant l'algorithme de compression
en tri de blocks de texte Burrows-Wheeler, et le codage Huffman. La
compression est considérablement meilleure que celle effectuée par les
plus conventionels compresseurs basés sur LZ77/LZ78, et approche la
performance de la famille PPM de compresseurs statistiques.

%description -l pl.UTF-8
Kompresor bzip2 używa algorytmu Burrows-Wheelera do kompresji danych i
metody Huffmana do ich kodowania. Kompresja pliku czy archiwum tar
jest z reguły lepsza niż w przypadku stosowania klasycznych
kompresorów LZ77/LZ78. Opcje linii poleceń są bardzo podobne do
poleceń GNU Gzip ale nie są identyczne.

%description -l pt_BR.UTF-8
Bzip2 é um programa de compressão/descompressão. Tipicamente o arquivo
compactado fica 20 a 30 por cento menor do que se fosse compactado com
o gzip.

Note que o bzip2 não entende os arquivos do bzip original, nem os
arquivos do gzip.

%description -l ru.UTF-8
bzip2 компрессирует файлы используя компрессирующий текстовый алгоритм
блочной сортировки Burrows-Wheeler и кодирование Huffman'а.
Достигаемая компрессия обычно существенно лучше достигаемой более
привычными компрессорами на основе LZ77/LZ78 и приближается к той,
которую обеспечивает семейство статистических компрессоров PPM.

%description -l uk.UTF-8
bzip2 компресує файли використовуючи текстовий алгоритм блочного
сортування Burrows-Wheeler та кодування Huffman'а. Компресія, яка
досягається bzip2, як правило краща за ту, що забезпечують
розповсюджені компресори на базі LZ77/LZ78 і наближається до тої, що
її забезпечує сімейство статистичних компресорів PPM.

%package static
Summary:	Static bzip2 library (cross MinGW32 version)
Summary(pl.UTF-8):	Statyczna biblioteka bzip2 (wersja skrośna MinGW32)
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
Static bzip2 library (cross MinGW32 version).

%description static -l pl.UTF-8
Statyczna biblioteka bzip2 (wersja skrośna MinGW32).

%package dll
Summary:	%{realname} - DLL library for Windows
Summary(pl.UTF-8):	%{realname} - biblioteka DLL dla Windows
Group:		Applications/Emulators

%description dll
%{realname} - DLL library for Windows.

%description dll -l pl.UTF-8
%{realname} - biblioteka DLL dla Windows.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1

%build
%{__make} \
	AR="%{target}-ar" \
	RANLIB="%{target}-ranlib" \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall \$(BIGFILES)"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_dlldir}}

install *.h $RPM_BUILD_ROOT%{_includedir}
install *.a $RPM_BUILD_ROOT%{_libdir}
install *.dll $RPM_BUILD_ROOT%{_dlldir}

%if 0%{!?debug:1}
%{target}-strip $RPM_BUILD_ROOT%{_dlldir}/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{_libdir}/*.a
%endif

# for compatibility
ln -sf libbz2.a $RPM_BUILD_ROOT%{_libdir}/libbzip2.a
ln -sf libbz2.dll.a $RPM_BUILD_ROOT%{_libdir}/libbzip2.dll.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/libbz2.dll.a
%{_libdir}/libbzip2.dll.a
%{_includedir}/bzlib*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libbz2.a
%{_libdir}/libbzip2.a

%files dll
%defattr(644,root,root,755)
%{_dlldir}/bzip2.dll
