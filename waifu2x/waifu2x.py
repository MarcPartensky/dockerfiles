#!/usr/bin/env python

import os
import re
import argparse
import subprocess
from pathlib import Path

def process_file(input_path, output_path, waifu_args, delete_original=False):
    """Exécute waifu2x-converter-cpp avec les arguments donnés"""
    cmd = [
        'waifu2x-converter-cpp',
        '-i', str(input_path),
        '-o', str(output_path)
    ] + waifu_args

    try:
        subprocess.run(cmd, check=True, stderr=subprocess.PIPE)
        print(f"✅ Converti : {input_path.name}")
        
        if delete_original:
            input_path.unlink()
            print(f"🗑️ Supprimé : {input_path.name}")
            
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur avec {input_path.name} : {e.stderr.decode()}")
        return False

def generate_output_name(input_path, pattern, replacement, output_dir):
    """Génère le nom de sortie avec la regex"""
    stem = input_path.stem
    new_stem = re.sub(pattern, replacement, stem)
    return output_dir / f"{new_stem}.png"

def process_recursive(input_path, output_dir, pattern, replacement, waifu_args, delete=False):
    """Traite récursivement tous les fichiers d'entrée"""
    processed = 0
    skipped = 0
    errors = 0

    for root, _, files in os.walk(input_path):
        for file in files:
            input_file = Path(root) / file
            output_file = generate_output_name(
                input_file, 
                pattern, 
                replacement, 
                output_dir / Path(root).relative_to(input_path)
            )

            output_file.parent.mkdir(parents=True, exist_ok=True)

            if not output_file.suffix:
                output_file = output_file.with_suffix('.png')

            if output_file.exists():
                print(f"⏩ Existe déjà : {output_file.name}")
                skipped += 1
                continue

            if process_file(input_file, output_file, waifu_args, delete):
                processed += 1
            else:
                errors += 1

    print(f"\nRésultat : {processed} traités, {skipped} ignorés, {errors} erreurs")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Wrapper pour waifu2x-converter-cpp")
    parser.add_argument('-i', '--input', type=Path, required=True)
    parser.add_argument('-o', '--output', type=Path)
    parser.add_argument('-p', '--pattern', default='.*', help="Regex pour le nom de sortie")
    parser.add_argument('-r', '--replacement', default='\g<0>', help="Remplacement regex")
    parser.add_argument('--delete', action='store_true', help="Supprimer les originaux")
    args, waifu_args = parser.parse_known_args()

    # Définir le dossier de sortie par défaut
    args.output = args.output or args.input

    # Traitement
    if args.input.is_dir():
        process_recursive(
            args.input,
            args.output,
            args.pattern,
            args.replacement,
            waifu_args,
            args.delete
        )
    else:
        output_file = generate_output_name(
            args.input,
            args.pattern,
            args.replacement,
            args.output.parent
        )
        process_file(args.input, output_file, waifu_args, args.delete)
