USE [FilmData]
GO

EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'UserRating'
GO

EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'ShootingTime'
GO

EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'PlayInfo'
GO

EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'PlayType'
GO

EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'Color'
GO

EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'PlayTime'
GO

EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'OtherENFilmName'
GO

EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'OtherCNFilmName'
GO

EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'FilmType'
GO

EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'Language'
GO

EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'Country'
GO

EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'Name'
GO

EXEC sys.sp_dropextendedproperty @name=N'MS_Description' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'Id'
GO

/****** Object:  Table [dbo].[Film1905]    Script Date: 2019/9/27 2:37:30 ******/
DROP TABLE [dbo].[Film1905]
GO

/****** Object:  Table [dbo].[Film1905]    Script Date: 2019/9/27 2:37:30 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Film1905](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[FilmId] [int] NULL,
	[Name] [nchar](255) NULL,
	[Country] [nchar](255) NULL,
	[Language] [nchar](255) NULL,
	[FilmType] [nchar](255) NULL,
	[OtherCNFilmName] [nchar](255) NULL,
	[OtherENFilmName] [nchar](255) NULL,
	[PlayTime] [nchar](255) NULL,
	[Color] [nchar](255) NULL,
	[PlayType] [nchar](255) NULL,
	[PlayInfo] [nvarchar](MAX) NULL,
	[ShootingTime] [nchar](255) NULL,
	[FilmingLocations] [nchar](255) NULL,
	[UserRating] [nchar](255) NULL,
 CONSTRAINT [PK_Film1905] PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'1905��Ӱ�����ݿ�' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'Id'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'��Ӱ����' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'Name'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'����' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'Country'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'����' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'Language'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'ӰƬ����' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'FilmType'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'����������' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'OtherCNFilmName'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'����������' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'OtherENFilmName'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'ʱ��' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'PlayTime'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'ɫ��' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'Color'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'�汾' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'PlayType'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'��ӳ��Ϣ' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'PlayInfo'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'����ʱ��' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'ShootingTime'
GO

EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'�û�����' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Film1905', @level2type=N'COLUMN',@level2name=N'UserRating'
GO


