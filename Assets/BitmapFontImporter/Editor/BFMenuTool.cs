﻿using UnityEngine;
using UnityEditor;

namespace litefeel
{

    public class BFMenuTool
    {
        [MenuItem("Assets/Bitmap Font/Regenerate Bitmap Font", true)]
        public static bool CheckGenerateFont()
        {
            TextAsset selected = Selection.activeObject as TextAsset;
            if (selected == null) return false;
            return BFImporter.IsFnt(AssetDatabase.GetAssetPath(selected));
        }

        [MenuItem("Assets/Bitmap Font/Regenerate Bitmap Font")]
        public static void GenerateFont()
        {
            TextAsset selected = Selection.activeObject as TextAsset;
            BFImporter.DoImportBitmapFont(AssetDatabase.GetAssetPath(selected));
        }


        [MenuItem("Assets/Bitmap Font/Regenerate All Bitmap Font")]
        public static void GenerateAllFont()
        {

        }
    }

}