#!/usr/bin/env sh
#fasta_to_reactions.sh - annotates a fna file to a reaction list using RAST

#If the shell complains about not being able to find the svr_* programs, you'll
#have to find out where they are installed as this line is apparently wrong.
#The attached Makefile should install it in this location.
export PATH="$PATH:$PREFIX/share/sas/bin"

#This is just a unix filter, so use stdin and stdout. stdin is a fasta file
#containing the assembled contigs (.fna) and the output is a newline-separated
#list of reactions (rxn#####).
svr_call_pegs \
    | svr_assign_using_figfams \
    | cut -f3 \
    | svr_roles_to_reactions \
    | cut -f2 \
    | sort \
    | uniq
