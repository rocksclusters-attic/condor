# $Id: Makefile,v 1.16 2012/11/27 00:48:55 phil Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 5.6 (Emerald Boa)
# 		         version 6.1 (Emerald Boa)
# 
# Copyright (c) 2000 - 2013 The Regents of the University of California.
# All rights reserved.	
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided 
# with the distribution.
# 
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement: 
# 
# 	"This product includes software developed by the Rocks(r)
# 	Cluster Group at the San Diego Supercomputer Center at the
# 	University of California, San Diego and its contributors."
# 
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.  The name of the
# software includes the following terms, and any derivatives thereof:
# "Rocks", "Rocks Clusters", and "Avalanche Installer".  For licensing of 
# the associated name, interested parties should contact Technology 
# Transfer & Intellectual Property Services, University of California, 
# San Diego, 9500 Gilman Drive, Mail Code 0910, La Jolla, CA 92093-0910, 
# Ph: (858) 534-5815, FAX: (858) 534-7345, E-MAIL:invent@ucsd.edu
# 
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# @Copyright@
#
# $Log: Makefile,v $
# Revision 1.16  2012/11/27 00:48:55  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.15  2012/05/06 05:48:57  phil
# Copyright Storm for Mamba
#
# Revision 1.14  2011/07/23 02:30:56  phil
# Viper Copyright
#
# Revision 1.13  2010/09/07 23:53:13  bruno
# star power for gb
#
# Revision 1.12  2009/05/01 19:07:14  mjk
# chimi con queso
#
# Revision 1.11  2008/12/10 21:37:40  bruno
# - condor roll is now buildable outside rocks source tree
#
# - updated bits to v7.0.5
#
# Revision 1.10  2008/10/18 00:56:06  mjk
# copyright 5.1
#
# Revision 1.9  2008/03/06 23:41:49  mjk
# copyright storm on
#
# Revision 1.8  2007/06/23 04:03:32  mjk
# mars hill copyright
#
# Revision 1.7  2006/09/11 22:47:55  mjk
# monkey face copyright
#
# Revision 1.6  2006/08/10 00:10:12  mjk
# 4.2 copyright
#
# Revision 1.5  2005/10/12 18:08:57  mjk
# final copyright for 4.1
#
# Revision 1.4  2005/09/16 01:02:33  mjk
# updated copyright
#
# Revision 1.3  2005/06/16 01:17:49  nadya
# give cat a full name
#
# Revision 1.2  2005/05/24 21:22:07  mjk
# update copyright, release is not any closer
#
# Revision 1.1  2005/03/23 20:43:07  nadya
# clean old entries, reorganize dirs
#
#


PKGROOT		= /opt/nmi
REDHAT.ROOT	= $(PWD)/../../

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk

version.mk: version.mk.in
	/bin/cat version.mk.in ../version.mk > version.mk

GLOBUS_LOCATION = /opt/nmi
GPT_LOCATION    = /opt/gpt
CONDOR_LOCATION	= /opt/condor
GLOBUS_FLAVOR	= gcc32

SEDSPEC += \
	-e 's%@GLOBUS_LOCATION@%$(GLOBUS_LOCATION)%g' \
	-e 's%@GPT_LOCATION@%$(GPT_LOCATION)%g' \
	-e 's%@CONDOR_LOCATION@%$(CONDOR_LOCATION)%g' \
	-e 's%@GLOBUS_FLAVOR@%$(GLOBUS_FLAVOR)%g' \
	-e 's%@VERSION_JOB_MANAGER_SETUP@%$(VERSION_JOB_MANAGER_SETUP)%g' \
	-e 's%@VERSION_REPORTER@%$(VERSION_REPORTER)%g' \
	-e 's%@VERSION_REPORTER_SETUP@%$(VERSION_REPORTER_SETUP)%g'


clean::
	rm -f version.mk

