import ldap

class PyLDAP():
	
	def __init__(self, host, base_dn, password):
		self.host = host
		self.base_dn = base_dn
		self.password = password
		try:
			self.conn = ldap.initialize(self.host)
			self.conn.simple_bind_s(self.base_dn, self.password)
		except ldap.LDAPError, e:
			print e
			
	def search(self, search_dn, search_scope, search_filter):
		try:
			ldap_result_id = self.conn.search(search_dn, search_scope, search_filter, None)
			
			result_set = []
			
			while 1:
				result_type, result_data = self.conn.result(ldap_result_id, 0)
				if result_data == []:
					break
				else:
					if result_type == ldap.RES_SEARCH_ENTRY:
						result_set.append(result_data)
			return result_set
			
		except ldap.LDAPError, e:
			print e
			
			return 'Error encountered'
			
if __name__ == '__main__':
	
	host = '<ldap host>'
	base_dn = '<base_dn>'
	password = ''
	
	ldap_con = PyLDAP(host, base_dn, password)
	
	results = ldap_con.search("<search dn>", ldap.SCOPE_SUBTREE, "<query>")
	
	print results
		
	
