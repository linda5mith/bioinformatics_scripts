df.sort_values(by=['qseqid','qseqid','sstart','send'],inplace=True)
s = df.groupby(['qseqid', 'sseqid'])['send'].shift()
df['length'] = df['sstart'].lt(s) * df['sstart'].sub(s.fillna(0)) + df['length']
