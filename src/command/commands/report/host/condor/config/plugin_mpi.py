# $Id: plugin_mpi.py,v 1.6 2012/11/27 00:48:55 phil Exp $
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
# $Log: plugin_mpi.py,v $
# Revision 1.6  2012/11/27 00:48:55  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.5  2012/05/06 05:48:54  phil
# Copyright Storm for Mamba
#
# Revision 1.4  2011/07/23 02:30:55  phil
# Viper Copyright
#
# Revision 1.3  2010/12/08 16:58:03  phil
# Add RANK parameter.
# Update docs on MPI support.
#
# Revision 1.2  2010/10/26 16:37:28  phil
# Fixes to really respect attributes.
#
# Revision 1.1  2010/09/15 23:40:03  phil
# Add the plugin capability of the Rocks command line to reporting the condor host config
#
# Revision 1.3  2009/05/01 19:07:00  mjk
# chimi con queso
#
# Revision 1.2  2009/04/23 17:12:29  bruno
# cleanup 'rocks remove host' command
#
# Revision 1.1  2009/03/13 22:19:56  mjk
# - route commands done
# - cleanup of rocks.host plugins
#
# Revision 1.2  2009/03/06 21:28:12  bruno
# need to look at node_attributes table.
#
# Revision 1.1  2008/12/18 20:01:33  mjk
# attribute commands
#

import rocks.commands

class Plugin(rocks.commands.Plugin):

	def provides(self):
		return 'condor-mpi'

	def setDedicated(self, host, kvstore): 

		# get the Condor_Master for the pool
		cm_fqdn = self.db.getHostAttr(host, 'Condor_Master')
		kvstore['DedicatedScheduler']  = '"DedicatedScheduler@%s"' % cm_fqdn
		kvstore['MPI_CONDOR_RSH_PATH'] = '$(LIBEXEC)'
		kvstore['STARTD_EXPRS']        = '$(STARTD_EXPRS), DedicatedScheduler'
		kvstore['CONDOR_SSHD'] = '/usr/sbin/sshd'
		kvstore['CONDOR_SSH_KEYGEN'] = '/usr/bin/ssh-keygen'
		kvstore['START']        = 'True'
		kvstore['RANK'] 	= 'Scheduler =?= $(DedicatedScheduler)'

	def run(self, argv):
		host, kvstore = argv
		# test if MPI is enabled for the host. If so, set up the
		# the correct config values in the key,value store
		mpi_enabled = self.db.getHostAttr(host, 'Condor_EnableMPI')
		if mpi_enabled is not None:
			if (mpi_enabled.lower() == 'true' or mpi_enabled.lower() == 'yes'):
				self.setDedicated(host,kvstore)

