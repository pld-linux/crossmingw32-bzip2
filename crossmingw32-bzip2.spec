%define		realname		bzip2
Summary:	Extremely powerful file compression utility - Ming32 cross version
Summary(es.UTF-8):   Un compresor de archivos con un nuevo algoritmo
Summary(fr.UTF-8):   Utilitaire de compression de fichier extrêmement puissant
Summary(pl.UTF-8):   Kompresor plików bzip2 - wersja skrośna dla Ming32
Summary(pt_BR.UTF-8):   Compactador de arquivo extremamente poderoso
Summary(uk.UTF-8):   Компресор файлів на базі алгоритму блочного сортування
Summary(ru.UTF-8):   Компрессор файлов на основе алгоритма блочной сортировки
Name:		crossmingw32-%{realname}
Version:	1.0.2
Release:	2
License:	BSD-like
Group:		Applications/Archiving
Source0:	ftp://sources.redhat.com/pub/bzip2/v102/%{realname}-%{version}.tar.gz
# Source0-md5:	ee76864958d568677f03db8afad92beb
Patch0:		%{name}.patch
URL:		http://sources.redhat.com/bzip2/
BuildRequires:	crossmingw32-gcc
Requires:	crossmingw32-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}

%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%ifarch alpha sparc sparc64 sparcv9
%define		optflags	-O2
%endif

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

%package dll
Summary:	%{realname} - DLL library for Windows
Summary(pl.UTF-8):   %{realname} - biblioteka DLL dla Windows
Group:		Applications/Emulators

%description dll
%{realname} - DLL library for Windows.

%description dll -l pl.UTF-8
%{realname} - biblioteka DLL dla Windows.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1

%build
CC=%{target}-gcc ; export CC
CXX=%{target}-g++ ; export CXX
LD=%{target}-ld ; export LD
AR=%{target}-ar ; export AR
AS=%{target}-as ; export AS
CROSS_COMPILE=1 ; export CROSS_COMPILE
CPPFLAGS="-I%{arch}/include" ; export CPPFLAGS
RANLIB=%{target}-ranlib ; export RANLIB
LDSHARED="%{target}-gcc -shared" ; export LDSHARED
TARGET="%{target}" ; export TARGET

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall \$(BIGFILES)"

rm -f libbz2.a libbz2.dll

$AR cru libbzip2.a blocksort.o huffman.o crctable.o randtable.o compress.o decompress.o bzlib.o
$RANLIB libbzip2.a

%{__cc} --shared libbzip2.a blocksort.o huffman.o crctable.o randtable.o compress.o decompress.o bzlib.o -Wl,--enable-auto-image-base -o bzip2.dll -Wl,--out-implib,libbzip2.dll.a

%if 0%{!?debug:1}
%{target}-strip *.dll
%{target}-strip -g -R.comment -R.note *.a
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{arch}/{include,lib}
install -d $RPM_BUILD_ROOT%{_datadir}/wine/windows/system

install *.h $RPM_BUILD_ROOT%{arch}/include
install *.a $RPM_BUILD_ROOT%{arch}/lib
install *.dll $RPM_BUILD_ROOT%{_datadir}/wine/windows/system

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{arch}/include/*
%{arch}/lib/*

%files dll
%defattr(644,root,root,755)
%{_datadir}/wine/windows/system/*
