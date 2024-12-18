delete from [Diseases] where id<=6
GO
SET IDENTITY_INSERT [Diseases] ON
insert into [Diseases] (id,title) values
	(1,'Blepharitis'), (2,'Conjunctivitis'), (3,'Corneal Dermoid'), (4,'Non-ulcerative Keratitis'), (5,'Corneal Ulcer'), (6,'Normal')
SET IDENTITY_INSERT [Diseases] OFF

	