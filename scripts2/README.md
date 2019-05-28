MFBA
====

Installation instructions
-------------------------

 1. Clone this repo and `cd` to it.
 2. Run `make install`.  
    If you don't have superuser rights on the host you're working on
    (which you probably don't), install it to a location outside of the
    system dirs (default is the GNU standard `/usr/local`). You can do
    this by running something like `make install PREFIX="~/.local"`. This
    has the disadvantage that you'll have to run this first every session:

        export PREFIX="$HOME/.local"
        export PATH="$PATH:$HOME/.local/bin:$HOME/.local/share/sas/bin"

    If you already have a writeable `$PREFIX` set this will not be a
    problem as the bundled programs will then do this path addition
    automatically.

Usage
-----
This program can be divided into two or three steps, as seen from a data
science standpoint. First there is a _map_ step, in which the input
fasta files are transformed to lists of reactions. This is done using
RAST annotation, and actually not by this program. A script for it is
included for ease of use, just use the `fna_to_rxn`. The last bit of the
mapping step is done with a tool called `rxn_expandinfo` which adds the
compounds in reactions to the file.

The second step is a _reduce_, or aggregation. In this step, done with
`rxn_to_connections`, the lists of compounds are connected to each
other. This creates a list of the form

    organism a  <TAB>  compound  <TAB>  organism b

where compound is created by organism a and used by organism b. This list
can really large (gigabytes). This list can then be processed further with
your own tools (one is supplied, which adds a weight to every connection
based on how rare it is, `connection_add_weight`). It can also be
converted into a table using the `lists_to_matrix` tool that is included.

A typical session will look something like this (`bash`):

    for fasta in *.fna; do 
        fna_to_rxn <$fasta | rxn_expandinfo >${fasta%.fna}.rxn
    done
    rxn_to_connections *.rxn | tee connections | lists_to_matrix -c3 >matrix

Now you have a file, `connections`, containing all the connections
within the ecosystem, and another, `matrix`, which has a connection
matrix counting them all. In this file, every row is a compound 'donor'
and every column an 'acceptor'. This can be visualized as a heatmap,
or clustered using your favourite R libraries.
