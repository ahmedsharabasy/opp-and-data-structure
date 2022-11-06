using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace كلاس_ينشئ_مجلد_تعليم
{
    class tools
    {
        public static void createFolder(string path)
        {
            Directory.CreateDirectory(path);
        }


        public static void createFolders(string[] paths)
        {
            foreach (string folder in paths)
            {
                createFolder(folder);
            }
        }

        public static void createEmptyFile(string path)
        {
            if (!File.Exists(path))
            {
                File.Create(path).Close();    // عشان يغلق الملف بعد انشائه وميغضلش مفتوح وانا مش عايزه
            }
        }


        public static void createEmptyFiles(string[] paths)
        {
            foreach(string file in paths)
            {
                createEmptyFile(file);
                //File.Create(file);
            }
        }

        //************************************************************************************************************************

        public static void createdatafile(string path,string[] lines)
        {
            StreamWriter sw = new StreamWriter(path);
            foreach(string line in lines)
            {
                sw.WriteLine(line);
                

            }
        }


        public static void createdatafiles(string[] paths,string[][] alllines)
        {
            for(int x =0; x<paths.Count();x++)
            {
                createdatafile(paths[x], alllines[x]);
            }
        }





    }
}
