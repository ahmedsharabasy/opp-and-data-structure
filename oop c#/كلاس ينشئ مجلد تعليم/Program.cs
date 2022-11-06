using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace كلاس_ينشئ_مجلد_تعليم
{
    class Program
    {
        static void Main(string[] args)
        {
            tools.createFolder("my folder");

            string[] folders = { "first folder", "second folder", "third folder" };
            tools.createFolders(folders);


            tools.createEmptyFile("my file.txt");

            string[] files = { "file 1.txt", "file 2.txt", "file 3.txt" };
            tools.createEmptyFiles(files);

            //**********************************************************************************************

            tools.createdatafile("my new file.txt", new string[] { "aaa", "sss", "ddd" });


            string[] filesname = { "my1.txt", "my2.txt", "my3.txt" };
            string[] files1 = { "welcome1", "hello1", "Hi1" };
            string[] files2 = { "welcome2", "hello2", "Hi2" };
            string[] files3 = { "welcome3", "hello3", "Hi3" };
            string[][] all = { files1, files2, files3 };

            tools.createdatafiles(filesname, all);

        }


    }
}
