"""Use function method simulate Class."""

def File(file_name, file_format, file_content):

    def init(file_name, file_format, file_content):
        file = {
            'name': file_name,
            'format': file_format,
            'content': file_content,
            'open': file_open,
            'read': file_read,
            'close': file_close,
        }
        return file


    def file_open(file):
        print('The {}.{} Opened.'.format(file['name'], file['format']))


    def file_read(file):
        print('Reading {}.{}...\nThe content is [{}]'.format(
            file['name'], file['format'], file['content'])
            )


    def file_close(file):
        print('The {0}.{1} Closed.'.format(file['name'], file['format']))

    return init(file_name, file_format, file_content)


def main():
    file1 = File('abc', 'txt', 'Hello world Demo')
    # print(file1)
    file1['open'](file1)
    file1['read'](file1)
    file1['close'](file1)

    file2 = File('music', 'mp4', 'This is song of Tay-tay.')
    # print(file2)
    file2['open'](file2)
    file2['read'](file2)
    file2['close'](file2)

if __name__ == '__main__':
    main()
