class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueemails = set()

        for email in emails:
            parts = email.split('@')

            uniqueemails.add(parts[0].split('+')[0].replace('.','')+'@'+parts[1])

        return len(uniqueemails)