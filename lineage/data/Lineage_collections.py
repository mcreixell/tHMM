""" This file is to collect those lineages that have the same condition, and have 3 or greater number of cells in their lineages. """

from ..LineageInputOutput import import_Heiser
from ..states.StateDistributionGaPhs import StateDistribution
from ..LineageTree import LineageTree

#----------------------- Control conditions from both old and new versions -----------------------#
desired_num_states = 2
E = [StateDistribution() for _ in range(desired_num_states)]


def popout_single_lineages(lineages):
    """ To remove lineages with cell numbers <= 5. """
    trimed_lineages = []
    for cells in lineages:
        if len(cells) < 5:
            pass
        else:
            trimed_lineages.append(cells)
    assert len(trimed_lineages) > 0
    return trimed_lineages


# -- Lapatinib control

lap01 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_A5_1_V5.xlsx")]
lap012 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_A5_2_V4.xlsx")]
lap02 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_A5_1_V4.xlsx")]
lap03 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_A5_1_V4.xlsx")]

Lapatinib_Control = lap01 + lap012 + lap02 + lap03
# used for when we want to writes states instead of phase lengths
len_lp_cntr = [len(lap01), len(lap012), len(lap02), len(lap03)]

# -- LAPATINIB 25 uMolars

lapb63 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_B6_1_V4.xlsx")]
lapb632 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_B6_2_V4.xlsx")]
lapb64 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_B6_1_V4.xlsx")]
lapb642 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_B6_2_V4.xlsx")]
lapb65 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_B6_1_V4.xlsx")]
lapb652 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_B6_2_V4.xlsx")]
lapb653 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_B6_3_V4.xlsx")]


Lapt25uM = lapb63 + lapb632 + lapb64 + lapb642 + lapb65 + lapb652 + lapb653
len_lp_25 = [len(lapb63), len(lapb632), len(lapb64), len(lapb642), len(lapb65), len(lapb652), len(lapb653)]

# -- LAPATINIB 50 uMolars

lapC501 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_C5_1_V4.xlsx")]
lapC502 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_C5_2_1_V4.xlsx")]
lapC503 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_C5_2_2_V4.xlsx")]
lapC504 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_C5_3_1.xlsx")]
lapC505 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_C5_3_2.xlsx")]
lapC506 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_C5_3_3.xlsx")]

lapC507 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_C5_1_V4.xlsx")]
lapC508 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_C5_2_V4.xlsx")]
lapC509 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_C5_3_V4.xlsx")]
lapC510 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_C5_4_V4.xlsx")]

lapC511 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_C5_1_V4.xlsx")]
lapC512 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_C5_2_V4.xlsx")]
lapC513 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_C5_3_1.xlsx")]
lapC514 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_C5_3_2.xlsx")]

Lapt50uM = lapC501 + lapC502 + lapC503 + lapC504 + lapC505 + lapC506 + lapC507 + \
    lapC508 + lapC509 + lapC510 + lapC511 + lapC512 + lapC513 + lapC514
len_lp_50 = [
    len(lapC501),
    len(lapC502),
    len(lapC503),
    len(lapC504),
    len(lapC505),
    len(lapC506),
    len(lapC507),
    len(lapC508),
    len(lapC509),
    len(lapC510),
    len(lapC511),
    len(lapC512),
    len(lapC513),
    len(lapC514)]

# -- LAPATINIB 250 uMolars
lapD51 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_D5_1_V4.xlsx")]
lapD54 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_D5_2_V4.xlsx")]
lapD57 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_D5_3_V4.xlsx")]
lapD52 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_D5_1_V4.xlsx")]
lapD55 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_D5_2_V4.xlsx")]
lapD53 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_D5_1_V4.xlsx")]
lapD56 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_D5_2_V4.xlsx")]
lapD58 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_D5_3_V4.xlsx")]

Lap250uM = lapD51 + lapD54 + lapD57 + lapD52 + lapD55 + lapD53 + lapD56 + lapD58
len_lp_250 = [len(lapD51), len(lapD54), len(lapD57), len(lapD52), len(lapD55), len(lapD53), len(lapD56), len(lapD58)]

# -- Gemcitabine control

gem04 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_A3_1_V4.xlsx")]
gem042 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_A3_2_V4.xlsx")]
gem043 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_A3_3_V4.xlsx")]
gem05 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_A3_1_V5.xlsx")]
gem052 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_A3_2_V4.xlsx")]
gem06 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_A3_1_V4.xlsx")]
gem062 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_A3_2_V4.xlsx")]

gemControl = gem04 + gem05 + gem06 + gem042 + gem052 + gem062 + gem043
Gemcitabine_Control = popout_single_lineages(gemControl)
len_gm_cntr = [len(gem04), len(gem05), len(gem06), len(gem042), len(gem052), len(gem062), len(gem043)]

# -- GEMCITABINE 5 uMolars

gemc33 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_C3_1_V4.xlsx")]
gemc332 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_C3_2_V4.xlsx")]
gemc34 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_C3_1_V4.xlsx")]
gemc342 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_C3_2_V4.xlsx")]
gemc35 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_C3_1_V5.xlsx")]
gemc352 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_C3_2_V4.xlsx")]

gem5uM = gemc33 + gemc332 + gemc34 + gemc342 + gemc35 + gemc352
Gem5uM = popout_single_lineages(gem5uM)
len_gm_5 = [len(gemc33), len(gemc332), len(gemc34), len(gemc342), len(gemc35), len(gemc352)]

# -- GEMCITABINE 10 uMolars

gemc401 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_C4_1_V5.xlsx")]
gemc402 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_C4_2_1_V4.xlsx")]
gemc403 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_C4_2_2_V4.xlsx")]
gemc404 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_C4_3_1_V5.xlsx")]
gemc405 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_C4_3_2_V4.xlsx")]
gemc406 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_C4_4_V4.xlsx")]

gemc407 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_C4_1_V4.xlsx")]
gemc408 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_C4_2_V4.xlsx")]
gemc409 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_C4_3_V4.xlsx")]
gemc410 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_C4_4_V4.xlsx")]

gemc411 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_C4_1_V4.xlsx")]
gemc412 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_C4_2_V4.xlsx")]
gemc413 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_C4_3_V4.xlsx")]
gemc414 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_C4_4_1.xlsx")]
gemc415 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_C4_4_2.xlsx")]

Gem10uM = gemc401 + gemc402 + gemc403 + gemc404 + gemc405 + gemc406 + gemc407 + \
    gemc408 + gemc409 + gemc410 + gemc411 + gemc412 + gemc413 + gemc414 + gemc415
len_gm_10 = [
    len(gemc401),
    len(gemc402),
    len(gemc403),
    len(gemc404),
    len(gemc405),
    len(gemc406),
    len(gemc407),
    len(gemc408),
    len(gemc409),
    len(gemc410),
    len(gemc411),
    len(gemc412),
    len(gemc413),
    len(gemc414),
    len(gemc415)]

# -- GEMCITABINE 30 uMolars

gemD31 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_D3_1_V4.xlsx")]
gemD34 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_D3_2_V4.xlsx")]
gemD37 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00601_D3_3_V4.xlsx")]
gemD32 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_D3_1_V4.xlsx")]
gemD35 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00701_D3_2_V4.xlsx")]
gemD33 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_D3_1_V4.xlsx")]
gemD36 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_D3_2_V4.xlsx")]
gemD38 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00801_D3_3_V4.xlsx")]

Gem30uM = gemD31 + gemD34 + gemD37 + gemD32 + gemD35 + gemD33 + gemD36 + gemD38
len_gm_30 = [len(gemD31), len(gemD34), len(gemD37), len(gemD32), len(gemD35), len(gemD33), len(gemD36), len(gemD38)]

# -- PACLITAXEL 2 uMolars

taxb40 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00602_B6_1_V4.xlsx")]
taxb402 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00602_B6_2_V4.xlsx")]
taxb41 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00702_B4_1_V4.xlsx")]
taxb412 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00702_B4_2_V4.xlsx")]
taxb42 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00802_B4_1_V4.xlsx")]
taxb422 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00802_B4_2_V4.xlsx")]

taxs = taxb40 + taxb402 + taxb41 + taxb412 + taxb42 + taxb422
Tax2uM = popout_single_lineages(taxs)

# --PACLITAXEL 7.5 uMolars

taxD301 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00602_D3_1_V4.xlsx")]
taxD302 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00602_D3_2_V4.xlsx")]

Tax7uM = taxD301 + taxD302
Tax7uM = popout_single_lineages(Tax7uM)
# -- PALBOCICLIB 250 uMolars
palbD11 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00602_D3_1_V4.xlsx")]
palbD12 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00702_D1_1_V4.xlsx")]
palbD13 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00802_D1_1_V4.xlsx")]
# replicates
palbD14 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00602_D3_2_V4.xlsx")]
palbD15 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00702_D1_2_V4.xlsx")]
palbD16 = [LineageTree(list_of_cells, E) for list_of_cells in import_Heiser(path=r"lineage/data/heiser_data/new_version/AU00802_D1_2_V4.xlsx")]

palb250uM = palbD11 + palbD12 + palbD13 + palbD14 + palbD15 + palbD16
Palbo250uM = popout_single_lineages(palb250uM)
