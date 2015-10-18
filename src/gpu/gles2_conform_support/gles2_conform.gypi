# Copyright (c) 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'gl2_extension_test_sources': [
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestCompressedETC1RGB8Texture.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestCompressedETC1RGB8Texture.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestCompressedPalettedTexture.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestCompressedPalettedTexture.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestConditionalQuery.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestConditionalQuery.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestDataType1010102.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestDataType1010102.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestDebug.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestDebug.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestDepth24.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestDepth24.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestDepth32.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestDepth32.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestDepthTexture.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestDepthTexture.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestDepthTextureCubeMap.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestDepthTextureCubeMap.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestEGLCreateContext.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestEGLCreateContext.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestEGLImage.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestEGLImage.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestEGLImageExternal.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestEGLImageExternal.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestElementIndexUINT.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestElementIndexUINT.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestFBORenderMipmap.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestFBORenderMipmap.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestFragmentPrecisionHigh.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestFragmentPrecisionHigh.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestFramebufferObject.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestFramebufferObject.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestMapBuffer.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestMapBuffer.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestOcclusionQuery.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestOcclusionQuery.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestPackedDepthStencil.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestPackedDepthStencil.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestPointSizeArray.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestPointSizeArray.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestPointSprite.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestPointSprite.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestRGB8RGBA8.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestRGB8RGBA8.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestReadFormat.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestReadFormat.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestRequiredInternalformat.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestRequiredInternalformat.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestStencil1.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestStencil1.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestStencil4.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestStencil4.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestStencil8.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestStencil8.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestSurfacelessContext.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestSurfacelessContext.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestTexture3D.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestTexture3D.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestTextureCompressionASTCLDR.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestTextureCompressionASTCLDR.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestTextureCompressionASTCLDRVectors.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestTextureFloat.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestTextureFloat.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestTextureFloatLinear.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestTextureFloatLinear.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestTextureNPOT.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestTextureNPOT.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestUtilp.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestUtilp.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestVertexArrayObject.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestVertexArrayObject.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestVertexHalfFloat.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestVertexHalfFloat.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestVisibilityQuery.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2ExtensionTests/GTFExtensionTestVisibilityQuery.h',
    ],
    'gl2_fixed_test_sources': [
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestBlend.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestBlend.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestBufferClear.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestBufferClear.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestBufferColor.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestBufferColor.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestBufferCorners.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestBufferCorners.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestBufferObjects.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestBufferObjects.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestClip.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestClip.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestColorRamp.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestColorRamp.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestCopyTexture.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestCopyTexture.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestDepthBufferClear.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestDepthBufferClear.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestDepthBufferFunctions.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestDepthBufferFunctions.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestDither.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestDither.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestDivideByZero.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestDivideByZero.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestGets.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestGets.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestMipmapsInterpolation.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestMipmapsInterpolation.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestMipmapsSelection.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestMipmapsSelection.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestPointRasterization.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestPointRasterization.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestPointSprites.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestPointSprites.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestPolygonCull.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestPolygonCull.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestScissor.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestScissor.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestStencilPlaneClear.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestStencilPlaneClear.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestStencilPlaneCorners.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestStencilPlaneCorners.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestStencilPlaneFunction.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestStencilPlaneFunction.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestStencilPlaneOperation.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestStencilPlaneOperation.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestTextureEdgeClamp.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestTextureEdgeClamp.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestTransformViewport.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestTransformViewport.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestTriangleRasterization.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestTriangleRasterization.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestTriangleTiling.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestTriangleTiling.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestUserClipPlanes.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestUserClipPlanes.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestVertexOrder.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestVertexOrder.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestViewportClamp.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedTestViewportClamp.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedUtilg.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedUtilg.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedUtilr.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2FixedTests/GTFFixedUtilr.h',
    ],
    'gl2_test_sources': [
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestAttributeGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestAttributeGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestBindAllAttributes.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestBindAllAttributes.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestCreateObjectGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestCreateObjectGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestDetachGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestDetachGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestFixedDataType.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestFixedDataType.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestFramebufferObjects.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestFramebufferObjects.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetAttachedObjects.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetAttachedObjects.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetAttributeLocation.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetAttributeLocation.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetBIFD.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetBIFD.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetExtensions.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetExtensions.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetProgramInfoLog.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetProgramInfoLog.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetProgramiv.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetProgramiv.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetShaderInfoLog.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetShaderInfoLog.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetShaderiv.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetShaderiv.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetUniform.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetUniform.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetVertexAttrib.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestGetVertexAttrib.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestMaxVertexAttrib.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestMaxVertexAttrib.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestMultipleShaders.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestMultipleShaders.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestRelinkProgram.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestRelinkProgram.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestUniform.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestUniform.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestUniformQueryGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestUniformQueryGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestVertexAttribPointer.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestVertexAttribPointer.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestVertexAttributes.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestVertexAttributes.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestVertexProgramPointSize.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL2Tests/GTFGL2TestVertexProgramPointSize.h',
    ],
    'gtf_es_sources': [
      # Bootstrapping files commented out. We have different bootstrapping
      # files for each platform.
      # Note: FilesDATA.h, FilesDATA.c, and FilesTOC.c are generated
      # by GTF_ES/glsl/GTF/mergeTestFilesToCSource.pl
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/FilesTOC.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFAttDataGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFAttDataGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFDepthRangeParamGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFDepthRangeParamGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFModelDataGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFModelDataGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFPointParamGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFPointParamGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFReadPixelsGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFReadPixelsGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFShaderDataGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFShaderDataGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFShaderTextGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFShaderTextGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFStateDataGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFStateDataGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFTexDataGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFTexDataGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFTexParamGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFTexParamGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFUniDataGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GL/GTFUniDataGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFArguments.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFArguments.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFCoverageDict.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFCoverageGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFCoverageGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFDict.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFDictBase.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFFileReader.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFFileReader.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFInitEGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFLog.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFLog.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFMain.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFMain.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFMatrix.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFMemFile.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFMemFile.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFModelData.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFModelData.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFPort.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFPort.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFString.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFStringUtils.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFStringUtils.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTest.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTest.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestBuildGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestBuildGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestCompareGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestCompareGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestComplexityGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestComplexityGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestCoverageGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestCoverageGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestDriver.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestDriver.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestElement.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestElement.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestExtension.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestExtension.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestFixedGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestFixedGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestGL2Test.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestGL2Test.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestRasterizationGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestRasterizationGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestShaderLoadGL.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestShaderLoadGL.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestUtil.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFTestUtil.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFVec.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFVecBase.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFVector.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFVersion.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFgl.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/GTFgl.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/MIMG.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/MIMG.h',
      #'<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/Win32Console.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/XmlUtils.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/XmlUtils.h',
      #'<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/eglNative.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/eglNative.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/egl_config_select.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/egl_config_select.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/eglu.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/eglu.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/eglut.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/eglut.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/gl2Native.c',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/gl2Native.h',
      '<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/gl2ext_missing.h',
      #'<(DEPTH)/third_party/gles2_conform/GTF_ES/glsl/GTF/Source/main.c',
      '<(SHARED_INTERMEDIATE_DIR)/gles2_conform_test_embedded_data/FilesDATA.c',
      '<(SHARED_INTERMEDIATE_DIR)/gles2_conform_test_embedded_data/FilesDATA.h',
      '<(SHARED_INTERMEDIATE_DIR)/gles2_conform_test_embedded_data/FilesTOC.c',
      '<@(gl2_extension_test_sources)',
      '<@(gl2_fixed_test_sources)',
      '<@(gl2_test_sources)',
    ],
  },
  # We cannot have any targets here because these tests are compiled against
  # multiple platforms - ANGLE, CommandBufferService, and Pepper. Each platform
  # has different EGL headers.
}

# Local Variables:
# tab-width:2
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=2 shiftwidth=2:
