%define		realname		bzip2
Summary:	Extremely powerful file compression utility - Ming32 cross version
Summary(es):	Un compresor de archivos con un nuevo algoritmo
Summary(fr):	Utilitaire de compression de fichier extrЙmement puissant
Summary(pl):	Kompresor plikСw bzip2 - wersja skro╤na dla Ming32
Summary(pt_BR):	Compactador de arquivo extremamente poderoso
Summary(uk):	Компресор файл╕в на баз╕ алгоритму блочного сортування
Summary(ru):	Компрессор файлов на основе алгоритма блочной сортировки
Name:		crossmingw32-%{realname}
Version:	1.0.1
Release:	1
License:	BSD-like
Group:		Applications/Archiving
Source0:	ftp://sources.redhat.com/pub/bzip2/v100/%{realname}-%{version}.tar.gz
Patch0:		crossmingw32-bzip2.patch
URL:		http://sources.redhat.com/bzip2/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	crossmingw32-gcc
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{realname}-%{version}-root-%(id -u -n)

%define		no_install_post_strip	1

%define		target			i386-mingw32
%define		target_platform 	i386-pc-mingw32
%define		arch			%{_prefix}/%{target}
%define		gccarch			%{_prefix}/lib/gcc-lib/%{target}
%define		gcclib			%{_prefix}/lib/gcc-lib/%{target}/%{version}

%define		__cc			%{target}-gcc
%define		__cxx			%{target}-g++

%description
Bzip2 compresses files using the Burrows-Wheeler block-sorting text
compression algorithm, and Huffman coding. Compression is generally
considerably better than that achieved by more conventional
LZ77/LZ78-based compressors, and approaches the performance of the PPM
family of statistical compressors. The command-line options are
deliberately very similar to those of GNU Gzip, but they are not
identical.

%description -l es
Bzip2 es un programa de compresiСn/descompresiСn. TМpicamente el
archivo compactado queda entre 20 la 30 por ciento menor de que se
fuera compactado con gzip. Observa que bzip2 no entiende los archivos
del bzip original, ni los archivos del gzip.

%description -l fr
Bzip2 compresse des fichiers en utilisant l'algorithme de compression
en tri de blocks de texte Burrows-Wheeler, et le codage Huffman. La
compression est considИrablement meilleure que celle effectuИe par les
plus conventionels compresseurs basИs sur LZ77/LZ78, et approche la
performance de la famille PPM de compresseurs statistiques.

%description -l pl
Kompresor bzip2 u©ywa algorytmu Burrows-Wheelera do kompresji danych i
metody Huffmana do ich kodowania. Kompresja pliku czy archiwum tar
jest z reguЁy lepsza ni© w przypadku stosowania klasycznych
kompresorСw LZ77/LZ78. Opcje linii poleceЯ s╠ bardzo podobne do
poleceЯ GNU Gzip ale nie s╠ identyczne.

%description -l pt_BR
Bzip2 И um programa de compressЦo/descompressЦo. Tipicamente o arquivo
compactado fica 20 a 30 por cento menor do que se fosse compactado com
o gzip.

Note que o bzip2 nЦo entende os arquivos do bzip original, nem os
arquivos do gzip.

%description -l ru
bzip2 компрессирует файлы используя компрессирующий текстовый алгоритм
блочной сортировки Burrows-Wheeler и кодирование Huffman'а.
Достигаемая компрессия обычно существенно лучше достигаемой более
привычными компрессорами на основе LZ77/LZ78 и приближается к той,
которую обеспечивает семейство статистических компрессоров PPM.

%description -l uk
bzip2 компресу╓ файли використовуючи текстовий алгоритм блочного
сортування Burrows-Wheeler та кодування Huffman'а. Компрес╕я, яка
досяга╓ться bzip2, як правило краща за ту, що забезпечують
розповсюджен╕ компресори на баз╕ LZ77/LZ78 ╕ наближа╓ться до то╖, що
╖╖ забезпечу╓ с╕мейство статистичних компресор╕в PPM.

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
CFLAGS="-I%{arch}/include -D_WIN32" ; export CFLAGS

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{arch}/bin

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=$RPM_BUILD_ROOT%{arch}
cp libbz2.dll $RPM_BUILD_ROOT%{arch}/bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{arch}
