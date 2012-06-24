%define		realname		bzip2
Summary:	Extremely powerful file compression utility - Ming32 cross version
Summary(es):	Un compresor de archivos con un nuevo algoritmo
Summary(fr):	Utilitaire de compression de fichier extr�mement puissant
Summary(pl):	Kompresor plik�w bzip2 - wersja skro�na dla Ming32
Summary(pt_BR):	Compactador de arquivo extremamente poderoso
Summary(uk):	��������� ���̦� �� ��ڦ ��������� �������� ����������
Summary(ru):	���������� ������ �� ������ ��������� ������� ����������
Name:		crossmingw32-%{realname}
Version:	1.0.2
Release:	1
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

%description -l es
Bzip2 es un programa de compresi�n/descompresi�n. T�picamente el
archivo compactado queda entre 20 la 30 por ciento menor de que se
fuera compactado con gzip. Observa que bzip2 no entiende los archivos
del bzip original, ni los archivos del gzip.

%description -l fr
Bzip2 compresse des fichiers en utilisant l'algorithme de compression
en tri de blocks de texte Burrows-Wheeler, et le codage Huffman. La
compression est consid�rablement meilleure que celle effectu�e par les
plus conventionels compresseurs bas�s sur LZ77/LZ78, et approche la
performance de la famille PPM de compresseurs statistiques.

%description -l pl
Kompresor bzip2 u�ywa algorytmu Burrows-Wheelera do kompresji danych i
metody Huffmana do ich kodowania. Kompresja pliku czy archiwum tar
jest z regu�y lepsza ni� w przypadku stosowania klasycznych
kompresor�w LZ77/LZ78. Opcje linii polece� s� bardzo podobne do
polece� GNU Gzip ale nie s� identyczne.

%description -l pt_BR
Bzip2 � um programa de compress�o/descompress�o. Tipicamente o arquivo
compactado fica 20 a 30 por cento menor do que se fosse compactado com
o gzip.

Note que o bzip2 n�o entende os arquivos do bzip original, nem os
arquivos do gzip.

%description -l ru
bzip2 ������������� ����� ��������� ��������������� ��������� ��������
������� ���������� Burrows-Wheeler � ����������� Huffman'�.
����������� ���������� ������ ����������� ����� ����������� �����
���������� ������������� �� ������ LZ77/LZ78 � ������������ � ���,
������� ������������ ��������� �������������� ������������ PPM.

%description -l uk
bzip2 �������դ ����� �������������� ��������� �������� ��������
���������� Burrows-Wheeler �� ��������� Huffman'�. ������Ӧ�, ���
����������� bzip2, �� ������� ����� �� ��, �� ������������
�����������Φ ���������� �� ��ڦ LZ77/LZ78 � ������������ �� �ϧ, ��
�� ��������դ Ӧ������� ������������ ��������Ҧ� PPM.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall \$(BIGFILES)"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=$RPM_BUILD_ROOT%{arch}

install libbz2.dll $RPM_BUILD_ROOT%{arch}/bin

%if 0%{!?debug:1}
%{target}-strip --strip-unneeded -R.comment -R.note $RPM_BUILD_ROOT%{arch}/bin/*.dll
%{target}-strip -g -R.comment -R.note $RPM_BUILD_ROOT%{arch}/lib/*.a
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{arch}/bin/libbz2.dll
%{arch}/lib/libbz2.a
%{arch}/include/bzlib.h
