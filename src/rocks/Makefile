# --------------------------------------------------- -*- Makefile -*- --
# $Id: Makefile,v 1.18 2012/11/27 00:48:55 phil Exp $
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
# Revision 1.18  2012/11/27 00:48:55  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.17  2012/05/06 05:48:58  phil
# Copyright Storm for Mamba
#
# Revision 1.16  2011/07/23 02:30:56  phil
# Viper Copyright
#
# Revision 1.15  2010/09/07 23:53:13  bruno
# star power for gb
#
# Revision 1.14  2010/03/03 17:24:39  phil
# 1st stab at automatic integration of condor node running in EC2 to local
# collector.
#
# Revision 1.13  2009/05/01 19:07:14  mjk
# chimi con queso
#
# Revision 1.12  2008/12/10 21:37:40  bruno
# - condor roll is now buildable outside rocks source tree
#
# - updated bits to v7.0.5
#
# Revision 1.11  2008/10/18 00:56:07  mjk
# copyright 5.1
#
# Revision 1.10  2008/03/06 23:41:49  mjk
# copyright storm on
#
# Revision 1.9  2007/06/23 04:03:32  mjk
# mars hill copyright
#
# Revision 1.8  2007/06/11 19:51:51  phil
# Remove explicit spec file. Use a more generic make file
#
# Revision 1.3  2007/06/07 23:08:25  phil
# Added some add examples and a small readme
#
# Revision 1.2  2007/06/07 22:00:59  phil
# Use the CentOS build of PVM
#

PROFILES = rocks-condor.sh rocks-condor.csh
INITFILES = rocks-condor ec2-condor-collector

PKGROOT		= /opt/condor
REDHAT.ROOT	= $(PWD)/../../

-include $(ROCKSROOT)/etc/Rules.mk
include Rules.mk
-include $(ROCKSROOT)/etc/python.mk
include python.mk

build:

install::
	mkdir -p $(ROOT)/etc/profile.d
	install -m555 $(PROFILES) $(ROOT)/etc/profile.d
	mkdir -p $(ROOT)/etc/rc.d/init.d
	install -m544 $(INITFILES) $(ROOT)/etc/rc.d/init.d

clean::
	rm -rf $(NAME)-$(VERSION)
