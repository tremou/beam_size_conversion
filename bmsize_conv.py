from radio_beam import Beam
from astropy.io import fits
header = fits.getheader('myfitsfile.fits')
my_beam = Beam.from_fits_header(header)
print my_beam
