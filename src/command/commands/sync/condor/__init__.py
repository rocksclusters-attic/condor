# $Id: __init__.py,v 1.2 2008/03/06 23:41:49 mjk Exp $
# 
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		            version 5.0 (V)
# 
# Copyright (c) 2000 - 2008 The Regents of the University of California.
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
# $Log: __init__.py,v $
# Revision 1.2  2008/03/06 23:41:49  mjk
# copyright storm on
#
# Revision 1.1  2007/07/11 21:09:41  phil
# Add rocks sync condor command.
# Read config variables from database on each condor sync.
#
#

import os
import time
import sys
import string
import rocks.file
import rocks.commands


class Command(rocks.commands.sync.command):
	"""
	This command will stop the Condor Daemons on a master host,
	re-read information from the Rocks configuration database, 
	reconfigure Condor base on this information, and restart Condor.
	<example cmd='sync condor'>
	Rebuild the Condor Configuration
	</example>
	"""

	def run(self, params, args):
		condorPost=os.path.normpath('/etc/rc.d/rocksconfig.d/post-90-condor-server')
		condorSvc='/sbin/service rocks-condor'
		cmd = '%s stop' % condorSvc
                for line in os.popen(cmd).readlines():
			print line,

		if os.path.exists(condorPost):
			os.remove(condorPost)

		os.chdir(os.path.dirname(condorPost))
                for line in os.popen('/usr/bin/co %s' % 
				os.path.basename(condorPost)).readlines():
			print line
		os.chmod(condorPost,0770)
		
		while self.condorActive() != 0:
			print "Waiting for Condor Processes to Exit."
			time.sleep(5)
		
		cmd = '%s start' % condorSvc
                for line in os.popen(cmd).readlines():
                     	print line, 
		
	def condorActive(self):
		numProcs=0	
		cProcs=os.popen('/bin/ps -elf | /bin/grep condor | /bin/grep -v condor')
		for line in cProcs.readlines():
			numProcs += 1
		return numProcs